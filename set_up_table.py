#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 16:55:37 2018

@author: zhangyu
"""

import pandas as pd
import numpy as np
import pickle


url_TPE = pickle.load(open("./data/url_list_5_25.dat", "rb"))
url_NTP = pickle.load(open("./data/url_list_5_25_NTP.dat", "rb"))

url_TP = url_TPE + url_NTP

length = len(url_TP)

rent_dict = {
        '編號':[0]*length,
        '價格':[0]*length,
        '坪數':[0]*length,
        '樓層':[0]*length,
        '總樓層數':[0]*length,
        '型態':[0]*length,
        '種類':[0]*length,
        '地址':[0]*length,
        '區':[0]*length,
        '押金':[0]*length,
        '車 位':[0]*length,
        '管理費':[0]*length,
        '最短租期':[0]*length,
        '身份要求':[0]*length,
        '開伙':[0]*length,
        '養寵物':[0]*length,
        '性別要求':[0]*length,
        '朝向':[0]*length,
        '格局':[0]*length,
        '產權登記':[0]*length,
        '桌子':[1]*length,
        '衣櫃':[1]*length,
        '床':[1]*length,
        '熱水器':[1]*length,
        '天然瓦斯':[1]*length,
        '電視':[1]*length,
        '冰箱':[1]*length,
        '冷氣':[1]*length,
        '洗衣機':[1]*length,
        '椅子':[1]*length,
        '沙發':[1]*length,
        '網絡':[1]*length,
        '第四台':[1]*length,
        '座標':[0]*length,
        '捷運站':[0]*length,
        '火車站':[0]*length,
}

rentDf = pd.DataFrame(rent_dict)

#抓取編號
for i in range(0,length):
    bianHao = url_TP[i][30:37]
    rentDf.xs(i)['編號'] = bianHao
    
pickle.dump(rentDf, open("./data/rent_table.dat", "wb"))
