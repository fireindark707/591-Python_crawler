library(tidyverse)

load("./result/TP_result_6_1_v3.Rdata")
TP_result_6_1 <- TP_result_6_1[,-c(1,5,36,26)]
TP_result_6_1 <- as.data.frame(TP_result_6_1)
TP_result_6_1 <- dplyr::filter(TP_result_6_1, 總價格<15000,總價格>4500)

#price <- TP_result_6_1$總價格
#price_round <- round(price/1000)*1000

#TP_result_6_1$總價格 <- as.character(price_round)

library(dummy)
TP_result_dummy <- dummy(TP_result_6_1)
TP_result_numeric <- TP_result_6_1[,c(4,11,32)]
TP_result_bind <- cbind(TP_result_dummy,TP_result_numeric)

#SVR
require(e1071)

data <- TP_result_bind

#split

smp.size = floor(0.8*nrow(data)) 
set.seed(516)                     
train.ind = sample(seq_len(nrow(data)), smp.size)
train = data[train.ind, ] # 80%
test = data[-train.ind, ] # 20%

#train

model = svm(formula = 總價格 ~ ., data = train, cost=5, epsilon = 0.1)

summary(model)

#predict
test.pred = predict(model, test)

#plot
test_matrix <- cbind(test$總價格,test.pred)

# 資料的原始值(黑點)
plot(test_matrix[,1], pch=16, xlab="X", ylab="Y")
# SVR的預測值(藍叉)
points(test_matrix[,2], pch=4, col="blue")

plot(test$總價格,test.pred)

print(sqrt(mean((test_matrix[,1] - test_matrix[,2])^2)))

