# 데이터 분할
# 내장 함수를 이용
credit.df <- read.csv("german_credit_dataset.csv",header=T,sep=',')

idx <- sample(3,nrow(credit.df), replace=T, prob=c(0.5,0.3,0.2))   # 1,2,3을 1000번 반복 추출, 5:3:2의 확률
idx
train <- credit.df[idx==1,]
validation <- credit.df[idx==2,]
test <- credit.df[idx==3,]

# caret 패키지를 이용
library(caret)
part <- createDataPartition(credit.df$credit.rating, times=1,p=0.7)
parts <- as.vector(part$Resample1)
train <- credit.df[parts,]
test <- credit.df[-parts,]


# 성과분석
predicted <- factor(c(1,0,0,1,1,1,0,0,0,1,1,1))
actual <- factor(c(1,0,0,1,1,0,1,1,0,1,1,1))
xtabs(~predicted+actual)
confusionMatrix(predicted, actual)

# ROC curve
library(ROCR)
set.seed(12345)
probability <- runif(100)
labels <- ifelse(probability>0.5 & runif(100)<0.4,1,2)
pred <- prediction(probability, labels)  # 예측값과 실제값을 넣음으로써 prediction객체 생성
perform_result <- performance(pred,'tpr','fpr')
plot(perform_result)


