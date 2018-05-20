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

driver.get("https://rent.591.com.tw")
driver.get("https://rent.591.com.tw/?kind=0&region=1")


for num in range(1,20):
    html = driver.page_source
    element = driver.find_element_by_class_name("pageNext")
    driver.execute_script("arguments[0].click();", element)

    page = BeautifulSoup(html, "lxml")
    nameList = page.findAll("h3")

    for name in nameList:
        url = name.a.attrs["href"]
        url = url.strip()
        url_list.append(url)
        print(url)
        
        
