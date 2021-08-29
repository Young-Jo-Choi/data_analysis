# 앙상블
# 여러 개의 예측모형들을 만든 후 예측모형들을 조합하여 하나의 최종 예측모형을 만드는 방법
# 학습방법이 가장 불안전한 decision tree에 주로 사용

# 랜덤포레스트 : 배깅의 개념과 feature의 임의 선택을 결합한 앙상블 기법

credit <- read.csv('credit_final.csv')
credit$credit.rating <- as.factor(credit$credit.rating)
idx <- sample(1:nrow(credit),nrow(credit)*0.7,replace=F)
train <- credit[idx,]
test <- credit[-idx,]


# 배깅 : 주어진 자료에서 여러 개의 bootstrap(단순복원추출) 자료를 생성하고 각 자료에 예측모형을 만든 후
#        결합하여 최종 예측모형을 만드는 방법, 가지치기를 하지 않고 최대로 성장한 decision tree를 이용

library(adabag)
bag <- bagging(credit.rating~.,  # 에러가 뜬다면 target이 factor형인지 체크해보자
               data=train,
               mfinal=15)    # 반복 또는 트리의 수는 15
names(bag)
sort(bag$importance,decreasing = T)
bag.trees <- bag$trees
bag.trees[[2]]

library(caret)
pred.bag <- predict(bag,test,type='class')
confusionMatrix(data=as.factor(pred.bag$class), reference=test$credit.rating, positive='1')

library(ROCR)
pred.bag.roc <- prediction(as.numeric(pred.bag$class),as.numeric(test[,1]))
plot(performance(pred.bag.roc,'tpr','fpr'))
abline(a=0,b=1,lty=2,col='black')
performance(pred.bag.roc, 'auc')@y.values


# 부스팅 : 예측력이 약한 모형(weak learner)들을 결합하여 강한 예측모형을 만드는 방법
# Adaboost는 이진분류 문제에서 랜덤 분류기보다 조금 더 좋은 분류기 n개에 각각 가중치를 설정하고 
#         n개의 분류기를 결합하여 최종 분류기를 만든다.(가중치의 합은 1)

library(adabag)
boost <- boosting(credit.rating~.,data=train, 
                  boos=T,      # 샘플의 가중치 여부, False의 경우 모든 관측치에 동일한 가중치 부여
                  mfinal=80)
names(boost)
sort(boost$importance,decreasing = T)
boost$weights    # 각 의사결정나무에 부여된 가중치 값 확인

pred.boos <- predict(boost,test,type='class')
confusionMatrix(data=as.factor(pred.boos$class), reference = test$credit.rating,positive='1')
pred.boos.roc <- prediction(as.numeric(pred.boos$class), as.numeric(test[,1]))
plot(performance(pred.boos.roc,'tpr','fpr'))
abline(a=0, b=1, lty=2, col='black')
performance(pred.boos.roc,'auc')@y.values


# 랜덤 포레스트 : 의사결정나무의 특징인 분산이 크다는 점을 고려하여 배깅과 부스팅보다 더 많은 무작위성을 주어
#                 약한 학습기들을 생성한 후 이를 선형 결합하여 최종 학습기를 만드는 방식 + feature의 임의 선택

library(randomForest)
rf.model <- randomForest(credit.rating~.,
                         data=train,
                         ntree=50,       # 사용할 트리의 수
                         mtry=sqrt(20),  # 사용할 변수의 개수(보통 분류는 sqrt(변수 개수), 회귀는 (변수 개수)/3)
                         importance=T)   # 변수중요도 결과 확인
rf.model
names(rf.model)
rf.model$importance
varImpPlot(rf.model)

pred.rf <- predict(rf.model, test[,-1],type='class')
confusionMatrix(data=pred.rf, reference=test[,1],positive='1')

pred.rf.roc <- prediction(as.numeric(pred.rf),as.numeric(test[,1]))
plot(performance(pred.rf.roc,'tpr','fpr'))
abline(a=0,b=1,lty=2,col='black')

# 예시
data(iris)
idx <- sample(1:nrow(iris), nrow(iris)*0.7, replace=F)
train.iris <- iris[idx,]
test.iris <- iris[-idx,]
rf.model.iris <- randomForest(Species~.,
                              ,data=train.iris,
                              ntree=50, mtry=sqrt(length(iris[,-1])),
                              importance=T)
pred.rf.iris <- predict(rf.model.iris, test.iris[-5], type='class')
confusionMatrix(data=pred.rf.iris, reference = test.iris[,"Species"])
