#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 16:55:37 2018

@author: zhangyu
"""

import pandas as pd
import numpy as np
import pickle
url_list = pickle.load(open("./data/url_list_5_20.dat", "rb"))

length = len(url_list)

rent_dict = {
        '編號':[0]*length,
        '價格':[0]*length,
        '坪數':[0]*length,
        '樓層':[0]*length,
        '總樓層數':[0]*length,
        '型態':[0]*length,
        '種類':[0]*length,
        '地址':[0]*length,
        '押金':[0]*length,
        '車位':[0]*length,
        '管理費':[0]*length,
        '最短租期':[0]*length,
        '養寵物':[0]*length,
        '身分要求':[0]*length,
        '性別要求':[0]*length,
        '朝向':[0]*length,
        '格局':[0]*length,
        '桌子':[0]*length,
        '衣櫃':[0]*length,
        '床':[0]*length,
        '熱水器':[0]*length,
        '天然瓦斯':[0]*length,
        '電視':[0]*length,
        '冰箱':[0]*length,
        '冷氣':[0]*length,
        '洗衣機':[0]*length,
        '椅子':[0]*length,
        '沙發':[0]*length,
        '網絡':[0]*length,
        '第四台':[0]*length
}

rentDf = pd.DataFrame(rent_dict)

#抓取編號
for i in range(0,length):
    bianHao = url_list[i][30:37]
    rentDf.xs(i)['編號'] = bianHao
    
pickle.dump(url_list, open("./data/rent_table.dat", "wb"))
