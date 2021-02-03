#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/20 17:14
# Author :A0025-江苏-小丹
# QQ:915155536
# File :req_photo2.py
#  ===========================
import requests
import parsel
url='https://game.gtimg.cn/images/lol/act/img/js/hero/1.js'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
res=requests.get(url=url,headers=headers)
res.encoding='gb2312'
data=parsel.Selector(res.text)
