#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/13 10:56
# Author :A0025-江苏-小丹
# QQ:915155536
# File :yaml_load.py
#  ===========================
import yaml

file = open('./data.yaml', 'r', encoding='utf-8')

data = yaml.load(stream=file,Loader=yaml.FullLoader)
print(type(data), data)
