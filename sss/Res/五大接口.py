#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/21 14:17
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo1.py
#  ===========================
import requests

# 接口关联
# 1)登录接口
url1 = 'http://39.98.138.157:5000/api/login'
data1 = {
    'username': 'admin',
    'password': '123456'
}
res1 = requests.post(url=url1, json=data1)
print(type(res1.json()), res1.json())  # res.json()，返回的为dict字典；  res.text,返回的是字符串str

# 2)获取用户信息接口
url2 = 'http://39.98.138.157:5000/api/getuserinfo'
headers = {'token': res1.json()['token']}
res2 = requests.get(url=url2, headers=headers)
print(type(res2.json()), res2.json())

# 3)获取商品信息接口
url3 = 'http://39.98.138.157:5000/api/getproductinfo'
params = {'productid': '8888'}
res3 = requests.get(url=url3, params=params)
print(type(res3.json()), res3.json())

# 4)添加购物车接口
url4 = 'http://39.98.138.157:5000/api/addcart'
headers = {'token': res1.json()['token']}
data4 = {
    'openid': res2.json()['data'][0]['openid'],
    'productid': res3.json()['data'][0]['productid'],
    'userid': res2.json()['data'][0]['userid']
}
res4 = requests.post(url=url4, json=data4, headers=headers)
print(type(res4.json()), res4.json())

#5）提交订单接口
url5 = 'http://39.98.138.157:5000/api/createorder'
headers = {'token': res1.json()['token']}
data5 = {
    'cartid': res4.json()['data'][0]['cartid'],
    'openid': res2.json()['data'][0]['openid'],
    'productid': res3.json()['data'][0]['productid'],
    'userid': res2.json()['data'][0]['userid']
}
res5 = requests.post(url=url5, json=data5, headers=headers)
print(type(res5.json()), res5.json())