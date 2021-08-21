# plot 함수의 인자를 바꾸는 방식으로 그릴 수 있으나 코드 실행 때마다 새 그래프가 그려지는 반면
# 아래에서 소개하는 함수들을 사용하면 기존에 만들어진 그래프에 점을 중첩하여 표현해준다.


# 점 그래프
plot(NULL, type='n',xlim=c(0,8),ylim=c(0,3),xlab='Petal.Length',ylab='Petal.Width',main='iris')
points(iris$Petal.Length, iris$Petal.Width, cex=0.5)

# 선 그래프
plot(NULL, type='n',xlim=c(0,20),ylim=c(0,20),main='선 그래프')
lty_list <- list(1,2,3,'solid','dotdash','twodash','longdash')
lwd_list <- list(NULL,NULL,NULL,NULL,1,2,3,4)
for(i in c(1:7)){
  lines(c(0,19-i*2),c(19-i*2,19-i*2),lty=lty_list[[i]],lwd=lwd_list[[i]])
}

data(cars)
cars_df <- as.data.frame(cars)
plot(cars_df, main = "Stopping distance versus Speed")
# lowess는 주변에 위치한 점들을 이용해 특정한 점을 추정하는 다항식을 찾는 것으로 '지역 가중 다항식 회귀'라고 한다.
# 비모수 회귀 함수 : lowess(), ksmooth(), smood.spline(), earth()
lines(lowess(cars_df))

# 직선 그래프(abline), x=v, y=h 형태 외에 y=ax+b와 같은 형태의 직선 역시 그릴 수 있다.
plot(cars_df, ylim=c(0,130),xlim=c(0,30),main='cars data')
cars_lm <- lm(dist~speed, data=cars)
abline(cars_lm,col='red')
abline(v=median(cars_df$speed), lty=3)
abline(h=median(cars_df$dist), lty=3)

# 곡선 그래프(curve)
?dnorm
curve(dnorm(x,mean=0,sd=1),from=-3, to=3, xlab="x", ylab="density", main="curve of dnorm")

# 막대 그래프(barplot)
barplot(table(Cars93$Cylinders),ylim=c(1,55),xlab="Cylinders",ylab="도수") # 단일 범주
barplot(table(Cars93$Origin, Cars93$Cylinders),beside=T,ylim=c(0,60),legend=T) # 여러 범주

# 히스토그램(hist) : breaks 인자 통해 구간의 개수 정하거나 임의의 구간을 벡터로 지정 가능
hist(iris$Petal.Length, breaks=5)

# 파이 차트
pie(table(Cars93$Cylinders),labels=c("first","second","third","fourth","fifth","sixth"))

# 산점도 행렬(pairs) : 행렬,데이터프레임과 같이 데이터를 입력하는 방식 / formula를 입력하는 방식
pairs(~Sepal.Length+Sepal.Width+Petal.Length+Petal.Width, data=iris, 
      col=c("red","green","blue")[iris$Species],
      pch=c('+','*','#')[iris$Species])
par(xpd=TRUE)
legend("bottom", as.vector(unique(iris$Species)),fill=c("red", "green3", "blue"))
