
# 단일표본 T-검정 : 모집단이 정규성 만족해야
library(MASS)

str(cats)
df <- as.data.frame(cats)
head(df)
table(df$Sex)

shapiro.test(df$Bwt)

# 정규분포를 만족하지 않으므로 wilcoxon테스트
mean(df$Bwt)

wilcox.test(cats$Bwt, mu=2.7,alternative = 'two.sided')

# 대응표본 T-검정 : 단일 모집단 내에서 두 번의 처리를 가했을 때의 평균을 비교한다.
# 모집단이 정규성 만족해야

before = c(7,3,4,5,2,1,6,6,5,4)
after = c(8,4,5,6,2,3,6,8,6,5)
t.test(before, after, alternative = 'two.sided',paired=T)

# 독립표본 T-검정 : 두 개의 독립된 모집단의 평균을 비교
# 두 모집단이 정규성 만족해야, 두 모집단이 등분산 가정을 만족해야
# 예시) 귀무가설 - 고양이들의 성별에 따른 평균 몸무게에는 통계적으로 유의한 차이가 없다.
var.test(Bwt~Sex, data=cats) #-귀무가설의 기각 -> 등분산을 만족하지 않음 
t.test(Bwt~Sex, data = cats, alternative='two.sided', var.equal = F)
