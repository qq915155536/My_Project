#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/4 20:30
# Author :A0025-江苏-小丹
# QQ:915155536
# File :api_demo.py
#  ===========================
import requests
import json

data = {'username': 'admin', 'password': '123456'}
# # print(type(data))
#
# # 把字典转化为json格式
# json_data = json.dumps(data)
# # print(json_data, type(json_data))
#
# headers = {'Content-Type': 'application/json'}
#
# url = 'http://39.98.138.157:5000/api/login'
#
# # res = requests.post(url=url, data=data, headers=headers)
#
# res = requests.post(url=url, json=data)

# print(res)
# print(res.status_code)
# print(res.raise_for_status())

# print(res.content)
# print(res.text)
# print(type(res.json()),res.json())
# print(res.raw)
# print(res.request.headers)
# content=json.loads(res.text)
# print(type(content),content)


# 登录
url = 'http://39.98.138.157:5000/api/login'
data2 = {"password": "123456", "username": "admin"}
data2=json.dumps(data2)   # 把字段转化为json字符串
headers={"Content-Type":"application/json"}

res2=requests.post(url=url,data=data2,headers=headers)
print(res2.status_code,res2.text)
