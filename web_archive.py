#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 18:24:33 2018

@author: zhangyu
"""

import urllib3
import pickle
from bs4 import BeautifulSoup
import time

import sys   
sys.setrecursionlimit(1000000) #递归设置为一百万  

http = urllib3.PoolManager()

url_list = pickle.load(open("./data/url_list_5_25_NTP.dat", "rb"))

length = len(url_list)

web_archive = list()

for i in range(0, length):
    url = "https:" + url_list[i]
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "lxml")
    time.sleep(0.5)
    web_archive.append(soup)
    print(i)

pickle.dump(web_archive, open("./data/web_archive_5_25_NTP.dat", "wb"))
