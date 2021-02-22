#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/22 10:29
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test_case2.py
#  ===========================
import pytest

#用mark标记，对用例进行分类管理

@pytest.mark.webui
def test_01():
    print('webui_01')

@pytest.mark.webui
def test_02():
    print('webui_02')

@pytest.mark.interface
def test_03():
    print('interface_01')

@pytest.mark.interface
def test_04():
    print('interface_02')

if __name__ == '__main__':
    pytest.main(['-s'])