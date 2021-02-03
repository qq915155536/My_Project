#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/11 10:25
# Author :A0025-江苏-小丹
# QQ:915155536
# File :md5_demo.py
#  ===========================
import hashlib

s='123456'
l=hashlib.md5(s.encode('utf-8'))
print(l.hexdigest() )


#md5加密函数
def my_md5(s):
    s=str(s)
    return hashlib.md5(s.encode('utf-8')).hexdigest()

res=my_md5('123456')
print(res)

