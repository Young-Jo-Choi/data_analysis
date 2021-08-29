# SVM

credit <- read.csv('credit_final.csv')
credit$credit.rating <- as.factor(credit$credit.rating)
idx <- sample(1:nrow(credit),nrow(credit)*0.7,replace=F)
train <- credit[idx,]
test <- credit[-idx,]

library(e1071)
tune.svm(credit.rating~., data=credit, 
         gamma=10^(-6:-1), 
         cost=10^(1:2))       # 6*2=12개의 조합에서 모수 조율이 이루어짐

svm.model <- svm(credit.rating~., data=train, kernel='radial',   # Gaussian RBF
                 gamma=0.01, cost=10)
summary(svm.model)

library(caret)
pred.svm <- predict(svm.model, test, type='class')
confusionMatrix(data=pred.svm, reference = test[,1], positive='1')

library(ROCR)
pred.svm.roc <- prediction(as.numeric(pred.svm),as.numeric(test[,1])) 
plot(performance(pred.svm.roc,'tpr','fpr'))
abline(a=0,b=1,lty=2, col='black')
performance(pred.svm.roc,'auc')@y.values


# Naive Bayes Classsification
# 데이터에서 변수들에 대한 조건부 독립을 가정하는 알고리즘
# 클래스에 대한 사전 정보와 데이터로부터 추출된 정보를 결합하고, 베이즈 정리를 이용하여 
# 어떤 데이터가 특정 클래스에 속하는지를 분류하는 알고리즘

library(e1071)
nb.model <- naiveBayes(credit.rating~., data=train, 
                       laplace=0)    # laplace 보정여부를 물음, default는 0으로 비활성화
nb.model

pred.nb <- predict(nb.model, test[,-1], type='class')
confusionMatrix(data=pred.nb, reference=test[,1], positive='1')

pred.nb.roc <-prediction(as.numeric(pred.nb),as.numeric(test[,1]))
plot(performance(pred.nb.roc,'tpr','fpr'))
abline(a=0,b=1,lty=2,col='black')
performance(pred.nb.roc,'auc')@y.values
