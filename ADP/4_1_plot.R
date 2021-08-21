# 시각화
methods("plot") # R객체에 따른 plot 변형 함수

library(MASS)
data("Cars93")
# 인자나 기능이 헷갈리면 help를 통해 도움 받을 수 있다.
x = Cars93$Length
y = Cars93$Weight
plot(x, y, xlab='Length',ylab='Weight', main='Cars93')
print(paste(range(x),range(y)))

plot(x, y, xlab='Length',ylab='Weight', main='Cars93',xlim=c(130,230),ylim=c(1600,4400),pch='*')
plot(x, y, xlab='Length',ylab='Weight', main='Cars93',xlim=c(130,230),ylim=c(1600,4400),cex=2,col='blue')

# plot 함수 그래프의 종류(type) : p(점), l(선), b(점과 선을 모두), o(점과 선 중첩), n(그래프 초기화)
temp_obj <- tapply(y, x, mean)
class(temp_obj)
length(unique(x))
length(temp_obj)
plot(temp_obj, xlab='Length', ylab='Weigth', type='o')
# 선그래프(l)에 대한 종류(lty)
plot(temp_obj, xlab='Length', ylab='Weigth', type='l', lty=4)

# 서식
plot(1:10, type='n', xlab="",ylab="")
# pch에 벡터 형태로 넣음으로써 여러 모양 표현 가능
legend("bottom",c("x1","x2"),pch=5:6,title="bottom legend",bg='gray')
legend(7.5,4,c("x3","x4"),pch=1:2,lty=7:8,title='사용자 지정')
