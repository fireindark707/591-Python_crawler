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

rentDf = pd.DataFrame(np.random.randn(length,30),columns = ['編號','價格','坪數','樓層','總樓層數','型態','種類','地址','押金','車位','管理費','最短租期','養寵物','身分要求','性別要求','朝向','格局','桌子','衣櫃','床','熱水器','天然瓦斯','電視','冰箱','冷氣','洗衣機','椅子','沙發','網絡','第四台'])

#抓取編號
for i in range(0,length):
    bianHao = url_list[i][30:37]
    rentDf.xs(i)['編號'] = bianHao
    
