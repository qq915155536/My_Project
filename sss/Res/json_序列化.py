#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/12 14:40
# Author :A0025-江苏-小丹
# QQ:915155536
# File :json_序列化.py
#  ===========================
import json

l = [1, 2, 'admin', True]

#序列化：把数据转化为json格式,json字符串
json_res=json.dumps(l)
print(type(json_res),json_res)



#反序列化，把json字符串转化为其他格式
res=json.loads(json_res)
print(type(res),res)



