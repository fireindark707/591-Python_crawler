remove_outliers <- function(x, na.rm = TRUE, ...) {
  qnt <- quantile(x, probs=c(.25, .75), na.rm = na.rm, ...)
  H <- 1.5 * IQR(x, na.rm = na.rm)
  y <- x
  y[x < (qnt[1] - 0.8*H)] <- NA
  y[x > (qnt[2] + H)] <- NA
  y
}

outlier_by_rent <- function(x){
  x <- mutate(x, 每坪租金 = 總價格/坪數)
  
  by_qu <- group_by(x, 區)
  rentPerPing <- remove_outliers(by_qu$每坪租金)
  x$每坪租金 <- rentPerPing
  
  rent <- remove_outliers(by_qu$總價格)
  x$總價格 <- rent
  
  size <- remove_outliers(by_qu$坪數)
  x$坪數 <- size
  
  x <- filter(x, is.na(每坪租金)==FALSE, is.na(總價格)==FALSE,is.na(坪數)==FALSE)
}

library(readr)
library(tidyverse)
library(foreign)

fenZuTao <- read_csv("processed_data/fenZuTao_6_1_v2.csv")
duLiTao <- read_csv("processed_data/duLiTao_6_1_v2.csv")
yaFang <- read_csv("processed_data/yaFang_6_1_v2.csv")

fenZuTao[,-1]
duLiTao[,-1]
yaFang[,-1]

fenZuTao_no_outlier <- outlier_by_rent(fenZuTao)
duLiTao_no_outlier <- outlier_by_rent(duLiTao)
yaFang_no_outlier <- outlier_by_rent(yaFang)

#plot(fenZuTao$總價格,fenZuTao$坪數)
#plot(duLiTao$總價格,duLiTao$坪數)
#plot(yaFang$總價格,yaFang$坪數)
#
#plot(fenZuTao_no_outlier$總價格,fenZuTao_no_outlier$坪數)
#plot(duLiTao_no_outlier$總價格,duLiTao_no_outlier$坪數)
#plot(yaFang_no_outlier$總價格,yaFang_no_outlier$坪數)

write.arff(fenZuTao_no_outlier,file = "./result/fenzuTao_6_1.arff")
write.arff(duLiTao_no_outlier,file = "./result/duLiTao_6_1.arff")
write.arff(yaFang_no_outlier,file = "./result/yaFang_6_1.arff")

