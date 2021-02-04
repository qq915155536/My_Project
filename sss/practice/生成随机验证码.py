#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/4 15:54
# Author :A0025-江苏-小丹
# QQ:915155536
# File :生成随机验证码.py
#  ===========================
import random

def make_code(size=4):
    """
    :param size:要生成的验证码位数，默认4
    97-122 对应 a-z
    :return:
    """
    res=''
    for i in range(size):
        s1=chr(random.randint(97,122))
        s2=str(random.randint(0,9))
        res+=random.choice([s1,s2])
    return res


# print(make_code(4))