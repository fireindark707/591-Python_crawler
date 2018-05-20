#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:45:36 2018

@author: zhangyu
"""

condition_text = condition_box.get_text()
strlist = condition_text.split('：')
yaJing = strlist[1].split('車')[0]
cheWei = strlist[2].split('管')[0]
guanLiFei = strlist[3].split('最')[0]
zuiDuan = strlist[4].split('開')[0]
kaiHuo = strlist[5].split('養')[0]
chongWu = strlist[6].split('身')[0]
shenFen = strlist[7].split('可')[0]
