#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/4/7 21:55
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test_case.py
#  ===========================
import pytest


def test_01():
    print('this is test_01')


def test_02():
    print('this is test_02')


def test_03():
    assert 2 < 1

if __name__ == '__main__':
    pytest.main(['-s','-v','-rA','--alluredir','F:\My_Project\sss\my_pytest3\my-report'])