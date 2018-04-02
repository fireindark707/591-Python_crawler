#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:46:42 2018

@author: zhangyu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html") 
bsObj = BeautifulSoup(html.read())
print(bsObj)
