#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 21:08:05 2018

@author: zhangyu
"""

# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import pickle

driver = webdriver.Chrome()

driver.get("https://rent.591.com.tw")
driver.get("https://rent.591.com.tw/?kind=2&region=1")
url_list = list()

#開始分頁面抓取各租屋URL
for num in range(1,10):
    #等待兩秒，避免頁面加載不完
    time.sleep(2)
    html = driver.page_source
    page = BeautifulSoup(html, "lxml")
    nameList = page.findAll("h3")
    #等待，確保class有出來，但是好像沒什麼用
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'pageNext')))
    driver.execute_script("arguments[0].click();", element)

    for name in nameList:
        url = name.a.attrs["href"]
        url = url.strip()
        url_list.append(url)
        print(url)

    
driver.get("https://rent.591.com.tw")
driver.get("https://rent.591.com.tw/?kind=3&region=1")

for num in range(1,10):
    time.sleep(2)
    html = driver.page_source
    page = BeautifulSoup(html, "lxml")
    nameList = page.findAll("h3")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'pageNext')))
    driver.execute_script("arguments[0].click();", element)

    for name in nameList:
        url = name.a.attrs["href"]
        url = url.strip()
        url_list.append(url)
        print(url)

driver.get("https://rent.591.com.tw")
driver.get("https://rent.591.com.tw/?kind=4&region=1")

for num in range(1,10):
    time.sleep(2)
    html = driver.page_source
    page = BeautifulSoup(html, "lxml")
    nameList = page.findAll("h3")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'pageNext')))
    driver.execute_script("arguments[0].click();", element)

    for name in nameList:
        url = name.a.attrs["href"]
        url = url.strip()
        url_list.append(url)
        print(url)

#編輯文件名（配合當前時間）
#i = datetime.datetime.now()
#i = i.isoformat()
#fileName = str("./data/"+"url_list_"+i+".dat")

#用Pickle保存檔案
pickle.dump(url_list, open("./data/url_list_5_20.dat", "wb"))

#讀取
url_list = pickle.load(open("./data/url_list_5_20.dat", "rb"))

        
