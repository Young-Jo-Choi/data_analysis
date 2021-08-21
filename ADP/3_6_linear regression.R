# 회귀 분석
# 선형회귀분석의 가정
# 1. 독립변수와 종속변수 간의 선형성
# 2. 오차의 등분산성, 독립성, 정규성
# 체크포인트 : 회귀계수에 대한 p-value, 모형의 설명력, 모형의 통계적 유의성(p-value)

library(MASS)
data("Cars93")

Cars93_lm <- lm(Price~EngineSize, data=Cars93)
summary(Cars93_lm)

par(mfrow=c(2,3))
plot(Cars93_lm,which=c(1:6))

idx<-sample(1:nrow(Cars93),5)
idx
test <- Cars93[idx,]
# newdata는 data.frame 형태로 넣어야
predict.lm(Cars93_lm,test,interval="none")
predict.lm(Cars93_lm,test,interval="confidence")
predict.lm(Cars93_lm,test,interval="prediction")

# 다중선형회귀분석
# 검토사항 : 데이터가 전제하는 가정을 만족시키는가, 모형 내 회귀계수가 유의한가, 설명력, 통계적 유의성,
#            모형이 데이터를 잘 적합하는가, 다중공선성(VIF : 허용오차의 역수, 10이상이면 심각하다고 판단)
# 범주형 독립변수는 일반적으로 dummy variable로 변환해 처리한다. 
# lm함수는 자동으로 범주형 변수를dummy variable로 변환
iris_lm <- lm(Petal.Length~Sepal.Length+Sepal.Width+Petal.Width+Species, data=iris)
summary(iris_lm)
Price_lm <- lm(Price~EngineSize+RPM+Weight,data=Cars93)
summary(Price_lm)


# 최적회귀방정식의 선택 : F통계량, AIC 과 같은 기준을 근거로 제거
# 단계적 변수선택 :  forward selection, backward selection, stepwise selection
# 벌점화 선택기준 : AIC 혹은 BIC 계산하여 그 값이 최소가 되는 모형 선택

# backward selection(후진제거법, t통계량 확인) ex) EngineSize,RPM,Width,Length 4개의 변수 사용
lm_a <- lm(Price~EngineSize+RPM+Width+Length,data=Cars93)
summary(lm_a)
# 유의확률이 가장 높은 변수(Width) 제거
lm_b <- lm(Price~EngineSize+RPM+Length,data=Cars93)
summary(lm_b)
# 유의확률이 가장 높은 변수(Length) 제거
lm_c <- lm(Price~EngineSize+RPM,data=Cars93)
summary(lm_c)  # 통계적으로 유의하나 결정계수로 봐서는 모형이 데이터를 잘 설명한다 말하기는 어렵다.

# 자동으로 변수 선택해주는 함수(step)
lm_result <- lm(Price~EngineSize+Horsepower+RPM+Width+Length+Weight,data=Cars93)
step(lm_result, direction="backward",k=2) # k=2이면 AIC 사용
