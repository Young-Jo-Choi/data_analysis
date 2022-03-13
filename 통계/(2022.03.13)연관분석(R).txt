# # 연관분석 
# 기업의 DB내에서 상품 구매, 서비스 등 일련의 거래 또는 사건들 간의 규칙을 발견하기 위해 적용
# 
# - 장바구니 분석 : 장바구니에 무엇이 '같이' 들어있는지 분석
# - 서열분석 : 'A를 산 다음 B를 산다.'
# ## 측도(A->B)
# - 지지도(support) : P(A∩B) : A와 B를 동시에 포함하는 거래의 비율
# - 신뢰도(confidence) : P(B|A)=지지도/P(A) : 항목 A를 포함하는 거래 중 A와 B가 같이 포함될 확률 
# - 향상도(lift) : P(B|A)/P(B)=P(A∩B)/P(A)P(B)=신뢰도/P(B)<br>
#   A가 구매되지 않았을때 품목 B의 구매확률에 비해 A가 구매됐을때 품목 B의 구매확률의 증가비
# 
# ## Apriori 알고리즘 
# 최소 지지도보다 큰 지지도 값을 갖는 품목의 집합을 빈발항목집합(frequent item set)이라고 한다.<br>
#   최소 지지도 이상의 빈발항목집합을 찾은 후 그것들에 대해서만 연관규칙을 계산한다.

library(arules)
id <- c(1,2,3,4,5,6)
gender <- c("FEMALE","MALE","FEMALE","FEMALE","MALE","FEMALE")
age <- c("age_20","age_20","age_40","age_30","age_40","age_30")
rank <- c("Gold","Silver","Silver","VIP","Gold","Gold")
mobile_app_use <- c('Y','Y','N','Y','N','Y')
re_order <- c('Y','N','N','Y','N','Y')
cust_tel <- cbind(id,gender,age,rank,mobile_app_use,re_order)
cust_tel <- as.data.frame(cust_tel)
cust_tel_1 <- subset(cust_tel, select = -c(id))
# apriori 수행 전에 as 함수를 통해 트랜잭션 형태로 변경
tran.cust <- as(cust_tel_1,'transactions')
tran.cust
# inspect 함수 : 트랜잭션 데이터로 변환된 결과 확인
inspect(tran.cust)


# 연관규칙분석
data("Groceries")
Groceries  # 이미 트랜잭션 형태
inspect(Groceries[1:3])

# 총 125개의 연관규칙이 생성되었음을 알 수 있음
rules <- apriori(Groceries, parameter=list(support=0.01, confidence=0.3)) # 최소지지도:0.01, 최소신뢰도:0.3

# 연관규칙분석 결과 확인, 좌항(lhs)을 구매했을때 우항(rhs)를 구매하는 규칙
# confidence가 높다는 것은 구매 품목들의 연관성이 높음을 의미
# lift가 높다는 것은 좌항의 제품을 구매할 때, 우항의 제품을 구매할 확률이 약 n배 가량 높음을 의미
inspect(sort(rules, by=c('confidence'),decreasing = T)[1:5])

# 중복가지치기 함수 구현(좌항에서 우항, 우항에서 좌항의 규칙이 겹치지 않도록)
prune.dup.rules <- function(rules){
  rules.subset.matrix <- is.subset(rules, rules, sparse=F)
  rules.subset.matrix[lower.tri(rules.subset.matrix, diag=T)] <- NA
  dup.rules <- colSums(rules.subset.matrix, na.rm=T) >=1
  pruned.rules <- rules[!dup.rules]
  return(pruned.rules)
}

metric.params <- list(supp=0.001, conf=0.5, minlen=2) #minlen은 좌우합을 합친 최소 물품수
rules <- apriori(data=Groceries, parameter = metric.params,
                 appearance = list(default='lhs', rhs='soda'),   # 우측의 soda를 사기 위해 좌항의 아이템을 찾는 것으로 설정
                 control=list(verbose=F))   # apriori 함수의 실행결과를 나타내지 않음
rules <- prune.dup.rules(rules)
rules <- sort(rules, decreasing = T, by='confidence')
rules
inspect(rules[1:5])
# 결과 : coffee와 misc.bevarages를 함께 구매할 경우 soda를 구매한다는 규칙의 confidence가 가장 높음


metric.params <- list(supp=0.001, conf=0.3, minlen=2)
rules <- apriori(data=Groceries, parameter = metric.params,
                 appearance = list(default='rhs', lhs=c('yogurt','sugar')),   # yogurt와 sugar를 구매했을 때, 우항의 아이템을 찾는다.
                 control=list(verbose=F))   # apriori 함수의 실행결과를 나타내지 않음
rules <- prune.dup.rules(rules)
rules <- sort(rules, decreasing = T, by='confidence')
rules
inspect(rules[1:5])
# 결과 : sugar를 구매하면 milk를 구매한다는 규칙의 confidence가 제일 높음