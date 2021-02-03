#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/10/20 16:07
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo.py
#  ===========================
import json
dict={'name':'admin','age':18}
print(type(dict),dict)
d=json.dumps(dict)
print(type(d),d)

l=json.loads(d)
print(type(l),l)
