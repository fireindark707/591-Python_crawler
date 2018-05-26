#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:45:36 2018

@author: zhangyu
"""
import pickle

rentDf = pickle.load(open("./data/rent_table.dat", "rb"))
colnames = ['押金', '車 位', '管理費', '最短租期', '身份要求', '開伙', '養寵物', '身分要求', '性別要求', '朝向', '格局', '產權登記']

condition = condition_box.findAll('li')

for item in condition:
    item = item.get_text()
    item_name = item.split('：')[0]
    item_content = item.split('：')[1]
    if item_name in colnames:
        rentDf.ix[0, item_name] = item_content
