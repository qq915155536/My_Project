#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/23 15:12
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test_case2.py
#  ===========================

from selenium import webdriver
import pytest
import time


def test_01():
    driver=webdriver.Chrome()
    driver.get('http://www.baidu.com')
    time.sleep(3)
    driver.quit()

def test_02():
    driver=webdriver.Chrome()
    driver.get('http://www.bilibili.com')
    time.sleep(3)
    driver.quit()

if __name__ == '__main__':
    # 2. 多线程用例并发插件：
    # pip install pytest-xdist
    # -n 2   启动2个线程
    pytest.main(['test_case2.py','-n','2'])