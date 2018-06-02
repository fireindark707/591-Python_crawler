library(readr)
library(tidyverse)

X2018_05_25_TP_result <- read_csv("../../result/2018-05-25-TP-result.csv")
X2018_05_28_TP_result <- read_csv("../../result/2018-05-28-TP-result.csv")
X2018_06_01_TP_result <- read_csv("../../result/2018-06-01-TP-result.csv")

X2018_05_25_TP_result <- X2018_05_25_TP_result[,-1]
X2018_05_28_TP_result <- X2018_05_28_TP_result[,-1]
X2018_06_01_TP_result <- X2018_06_01_TP_result[,-1]

TP_rent_result <- rbind(X2018_05_25_TP_result,X2018_05_28_TP_result,X2018_06_01_TP_result)

TP_rent_result <- arrange(TP_rent_result, 編號)
TP_rent_result <- filter(TP_rent_result, 編號!=0, 價格!=0, 最短租期!=0, is.na(現況)==FALSE)
TP_rent_result <- filter(TP_rent_result, 編號!=6403638, 押金 %in% c("一個月", "二個月", "三個月", "面議", "其他"))

TP_rent_result <- mutate(TP_rent_result, 總價格 = 價格+管理費)
TP_rent_result <- select(TP_rent_result, -c(種類, 朝向, 座標, 價格, 管理費, 產權登記, 總樓層數))

TP_rent_result_filtered <- TP_rent_result[!duplicated(TP_rent_result$編號), ]

yaFang <- filter(TP_rent_result_filtered, 現況 == "雅房")
fenZuTao <- filter(TP_rent_result_filtered, 現況 == "分租套房")
duLiTao <- filter(TP_rent_result_filtered, 現況 == "獨立套房")

write.csv2(yaFang,file="yaFang_6_1.csv")
write.csv2(fenZuTao,file="fenZuTao_6_1.csv")
write.csv2(duLiTao,file="duLiTao_6_1.csv")