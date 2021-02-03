#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/11 11:18
# Author :A0025-江苏-小丹
# QQ:915155536
# File :mock_demo.py
#  ===========================
from unittest import mock


def f1(a, b):
    """
    :param a: 第一个参数
    :param b: 第二个参数
    :return: a+b
    """
    pass


print(f1(1, 2))

f1 = mock.Mock(return_value={'code': '1', 'meg': '登录失败！'})
print(f1(1, 2))

