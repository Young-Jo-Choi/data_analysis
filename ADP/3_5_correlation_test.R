# 상관분석

# 피어슨 상관계수 : 두 연속형 자료가 모두 정규성을 따른다는 가정 하에 선형적인 상관관계를 측정
# 스피어만 상관계수 : 실제 값을 사용하는 대신 데이터에 순위 매긴 후 그 순위에 대한 상관계수 산출하는 비모수적 방법
# 켄달의 상관계수 : 데이터의 순서쌍 X_i, Y_i에 대해 X_i가 커짐에 따라 Y_i가 커지면 부합, 반대일 경우 비부합으로 본다.
#                   전체 데이터에서 비부합쌍에 대한 부합쌍의 비율로 상관계수 추출 (-1 ~ 1)
#                   1일 경우 부합쌍의 비율이 100%, -1일 경우 비부합쌍의 비율이 100%, 0일 경우 X,Y는 상관 없음

# 귀무가설 : 변수X, 변수 Y간에는 상관 관계가 없다. (상관계수=0)
data("airquality")
df <- as.data.frame(airquality)
str(df)

air <- df[,c(1:4)]
# 계산
pearson_cor <- cor(air, use='pairwise.complete.obs', method='pearson')

cor(air, use='pairwise.complete.obs', method='kendall')

cor(air, use='pairwise.complete.obs', method='spearman')

pairs(air)
pairs(pearson_cor)

library(corrplot)
corrplot(pearson_cor)

cor.test(air$Ozone, air$Wind, method='pearson')
# 귀무가설을 기각하므로 -0.6015를 상관계수로 활용할 수 있다.
