#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/8/14 23:36
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test1.py
#  ===========================
import requests
import json
from jsonpath import jsonpath

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"
}
res = requests.get(url=url, headers=headers)
dict_data=res.json()
print(type(dict_data))
print(jsonpath(dict_data, '$..A..name'))
