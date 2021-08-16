# 분산분석(ANOVA)
# T검정이 두 집단 간 평균 차이를 비교하는 통계분석 방법이라면, 
# 분산분석은 두 개 이상의 다수 집단 간 평균을 비교하는 방법

# 사후 검정 : 분산분석 결과 귀무가설이 기각되었을 경우

# one-way ANOVA : 반응값에 대한 하나의 범주형 변수의 영향을 알아보기 위한 검증
# 모집단 수에 제한이 없으며, 각 표본의 수는 같지 않아도 된다.
# 등분산 가정과 정규성 검정을 만족해야한다.
# 귀무가설 : k개의 집단 간 모평균에 차이가 없다.

data(iris)
result <- aov(Sepal.Width~ Species, data=iris)
summary(result)  # 귀무가설 기각 -> 각 평균이 모두 동일하지는 않아
# 사후검정 : 어떤 종들 간 평균 차이가 있는지 파악
TukeyHSD(result)


# Two-way ANOVA : 반응값에 대해 두 개의 범주형 변수 A,B의 영향 알아보기 위한 검증
# 두 독립변수 A,B가 상관관계에 있는지를 살펴보는 교호작용에 대한 검증이 반드시 진행되어야한다.
# 교호작용 :  두 독립변수의 범주들의 조합으로 인해 반응변수에 미치는 특별한 영향
# 등분산 가정과 정규성 검정을 만족해야한다.
# 귀무가설1 : alpha 변수에 의한 종속변수 값에 차이가 없다.
# 귀무가설2 : beta 변수에 의한 종속변수 값에 차이가 없다.
# 귀무가설3 : alpha와 beta 변수의 상호작용 효과가 없다.

data('mtcars')
str(mtcars)

# aov함수 사용시 그룹을 구분하는 기준 변수는 반드시 팩터형
mtcars$cyl <- as.factor(mtcars$cyl)
mtcars$am <- as.factor(mtcars$am)
car <- mtcars[,c('cyl','am','mpg')]
str(car)

car_aov <- aov(mpg~cyl*am ,car)
summary(car_aov)
# cyl 변수에 대해서는 귀무가설 기각
# am 변수에 대해서는 귀무가설을 기각하지 않는다.
# 두 변수의 상호작용효과에 대해서는 귀무가설을 기각하지 않는다. :=교호작용 존재 X

interaction.plot(car$cyl, car$am, car$mpg, col = c('red','blue'))
# 일반적으로 상호작용 그래프에서 두 선이 서로 교차하고 있을 시에는
# x 축의 독립변수와 시각화된 독립변수 간에는 상호작용이 존재한다고 해석할 수 있다.