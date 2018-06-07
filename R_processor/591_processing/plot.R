load("./result/TP_result_6_1_v3.Rdata")
library(ggplot2)
library(tidyverse)

#繪製每坪租金分佈圖
ggplot(data  = TP_result_6_1) +
  geom_histogram(mapping = aes(x = 每坪租金, fill = 現況)) +
  theme(text = element_text(family = 'SimSun'))

ggplot(data = TP_result_6_1)+
  geom_boxplot(mapping = aes(x = 現況, y = 每坪租金, fill = 現況))+
  theme(text = element_text(family = 'SimSun'))

ggplot(data = TP_result_6_1_NewTaipei)+
  geom_point(mapping = aes(x = 坪數, y = 總價格, color = 現況), position = "jitter")+
  geom_smooth(mapping = aes(x = 坪數, y = 總價格, linetype = 現況))+
  theme(text = element_text(family = 'SimSun'))
#繪製總價格分佈圖
ggplot(data  = TP_result_6_1) +
  geom_histogram(mapping = aes(x = 總價格, fill = 現況)) +
  theme(text = element_text(family = 'SimSun'))

#配備count製表
peiBei <- tribble(
  ~房屋配備特性, ~percent,
  "冷氣", nrow(TP_result_6_1[TP_result_6_1$冷氣==1,])/nrow(TP_result_6_1),
  "冰箱", nrow(TP_result_6_1[TP_result_6_1$冰箱==1,])/nrow(TP_result_6_1),
  "天然瓦斯",  nrow(TP_result_6_1[TP_result_6_1$天然瓦斯==1,])/nrow(TP_result_6_1),
  "床", nrow(TP_result_6_1[TP_result_6_1$床==1,])/nrow(TP_result_6_1),
  "有陽臺", nrow(TP_result_6_1[TP_result_6_1$有陽臺==1,])/nrow(TP_result_6_1),
  "樓中樓", nrow(TP_result_6_1[TP_result_6_1$樓中樓==1,])/nrow(TP_result_6_1),
  "近捷運站", nrow(TP_result_6_1[TP_result_6_1$捷運站==1,])/nrow(TP_result_6_1),
  "桌子", nrow(TP_result_6_1[TP_result_6_1$桌子==1,])/nrow(TP_result_6_1),
  "椅子", nrow(TP_result_6_1[TP_result_6_1$椅子==1,])/nrow(TP_result_6_1),
  "沙發", nrow(TP_result_6_1[TP_result_6_1$沙發==1,])/nrow(TP_result_6_1),
  "洗衣機", nrow(TP_result_6_1[TP_result_6_1$洗衣機==1,])/nrow(TP_result_6_1),
  "熱水器", nrow(TP_result_6_1[TP_result_6_1$熱水器==1,])/nrow(TP_result_6_1),
  "第四台", nrow(TP_result_6_1[TP_result_6_1$第四台==1,])/nrow(TP_result_6_1),
  "網路", nrow(TP_result_6_1[TP_result_6_1$網路==1,])/nrow(TP_result_6_1),
  "衣櫃", nrow(TP_result_6_1[TP_result_6_1$衣櫃==1,])/nrow(TP_result_6_1),
  "電視", nrow(TP_result_6_1[TP_result_6_1$電視==1,])/nrow(TP_result_6_1)
)

peiBei$房屋配備特性 <- reorder(peiBei$房屋配備特性, peiBei$percent)

ggplot(data = peiBei)+
  geom_bar(mapping = aes(x = 房屋配備特性,y=percent),fill = "orange", stat = "identity")+
  theme(text = element_text(family = 'SimSun'))

#分區繪製租金表
TP_result_6_1_Taipei <- filter(TP_result_6_1, 區 %in% c("中正區",
                                                       "大同區",
                                                       "中山區",
                                                       "松山區",
                                                       "大安區",
                                                       "萬華區",
                                                       "信義區",
                                                       "士林區",
                                                       "北投區",
                                                       "內湖區",
                                                       "南港區",
                                                       "文山區"))
TP_result_6_1_NewTaipei <- filter(TP_result_6_1, 區 %in% c("三重區",
                                                          "板橋區",
                                                          "中和區",
                                                          "永和區",
                                                          "新莊區",
                                                          "土城區",
                                                          "蘆洲區",
                                                          "汐止區",
                                                          "樹林區",
                                                          "鶯歌區",
                                                          "三峽區",
                                                          "淡水區",
                                                          "新店區",
                                                          "深坑區",
                                                          "石碇區",
                                                          "坪林區",
                                                          "烏來區",
                                                          "瑞芳區",
                                                          "貢寮區",
                                                          "雙溪區",
                                                          "平溪區",
                                                          "五股區",
                                                          #"八里區",
                                                          "林口區",
                                                          "金山區",
                                                          "萬里區",
                                                          "三芝區",
                                                          "石門區",
                                                          "泰山區"))

  #臺北繪圖
ggplot(data = TP_result_6_1_Taipei)+
  geom_point(mapping = aes(x = 坪數, y = 總價格, color = 現況), position = "jitter")+
  geom_smooth(mapping = aes(x = 坪數, y = 總價格, linetype = 現況))+
  facet_wrap(~區)+
  theme(text = element_text(family = 'SimSun'))

  #新北繪圖
ggplot(data = TP_result_6_1_NewTaipei)+
  geom_point(mapping = aes(x = 坪數, y = 總價格, color = 現況), position = "jitter")+
  geom_smooth(mapping = aes(x = 坪數, y = 總價格, linetype = 現況))+
  facet_wrap(~區,nrow =4)+
  theme(text = element_text(family = 'SimSun'))

 #建築型態繪圖
TP_result_6_1_building <- filter(TP_result_6_1, 型態 %in% c("電梯大樓","透天厝","公寓"))

ggplot(data = TP_result_6_1_building)+
  geom_boxplot(mapping = aes(x = 型態, y = 總價格, fill = 現況))+
  theme(text = element_text(family = 'SimSun'))

#性別要求繪圖
ggplot(data = TP_result_6_1)+
  geom_boxplot(mapping = aes(x = 性別要求, y = 每坪租金, fill = 現況))+
  theme(text = element_text(family = 'SimSun'))

#樓層繪圖
ggplot(data = TP_result_6_1)+
  geom_boxplot(mapping = aes(x = 樓層, y = 總價格, fill = 現況))+
  theme(text = element_text(family = 'SimSun'))

#沙發繪圖
TP_result_6_1$沙發 <- factor(TP_result_6_1$沙發)
ggplot(data = TP_result_6_1)+
  geom_boxplot(mapping = aes(x = 沙發, y = 總價格, fill = 現況))+
  theme(text = element_text(family = 'SimSun'))

#性別要求計量
ggplot(data  = TP_result_6_1) +
  geom_histogram(mapping = aes(x = 性別要求, fill = 現況),stat= "count") +
  theme(text = element_text(family = 'SimSun'))
#建築型態計量
ggplot(data  = TP_result_6_1) +
  geom_histogram(mapping = aes(x = 型態, fill = 現況),stat= "count") +
  theme(text = element_text(family = 'SimSun'))