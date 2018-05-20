#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:08:05 2018

@author: zhangyu
"""

# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://rent.591.com.tw/?kind=0&region=1")
html = driver.page_source

page = BeautifulSoup(html, "lxml")
nameList = page.findAll("h3")

url_list = []
for name in nameList:
    url = name.a.attrs["href"]
    url_list.append(url)
    print(url)
