# 로지스틱 회귀

credit <- read.csv("credit_final.csv")
class(credit$credit.rating)
credit$credit.rating <- as.factor(credit$credit.rating) # 종속변수의 factor변
str(credit)
table(credit$credit.rating)

idx <- sample(1:nrow(credit),nrow(credit)*0.7,replace=F)
train <- credit[idx,]
test <- credit[-idx,]

logistic <- glm(credit.rating~., data=train, family='binomial') # family는 분석에 따른 link function
summary(logistic)   # p-value를 보고 변수 재선택

full_names=''
for (name in names(credit)){
  full_names = paste(full_names,'+', name)  
}
full_names

step.logistic <- step(glm(credit.rating~1, data=train, family='binomial'),
                      scope=list(lower=~1, upper=~credit.rating + account.balance +
                                   credit.duration.months + previous.credit.payment.status + 
                                   credit.purpose + credit.amount + savings + employment.duration +
                                   installment.rate + marital.status + guarantor + residence.duration + 
                                   current.assets + age + other.credits + apartment.type + 
                                   bank.credits + occupation + dependents + telephone + foreign.worker), 
                      direction='both')  #수정
summary(step.logistic)

library(caret)
pred <- predict(step.logistic, test[,-1],type='response')
prediction <- as.data.frame(pred)
prediction$grade <- ifelse(prediction$pred<0.5, 0,1)

confusionMatrix(data=as.factor(prediction$grade), reference=test[,1],positive='1')

library(ROCR)
pred.logistic.roc <- ROCR::prediction(as.numeric(prediction$grade),as.numeric(test[,1]))
plot(performance(pred.logistic.roc,'tpr','fpr'))
abline(a=0,b=1,lty=2,col='black')
performance(pred.logistic.roc,'auc')@y.values

# 다항 로지스틱 회귀분석(multinom)
# iris 데이터로 살핌
idx <- sample(1:nrow(iris),nrow(iris)*0.7,replace=FALSE)
train.iris <- iris[idx,]
test.iris <- iris[-idx,]

library(nnet)
mul.iris <- multinom(Species~., data=train.iris)

pred.mul <- predict(mul.iris,test.iris[,-5])
confusionMatrix(pred.mul, test.iris[,5])
