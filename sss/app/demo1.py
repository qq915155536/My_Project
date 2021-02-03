#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/19 14:47
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo1.py
#  ===========================
from appium import webdriver
import time

# 配置信息
# info = {
#     "platformName": "Android",  # 平台名
#     "platformVersion": "7.1.2",  # 平台版本号
#     "deviceName": "127.0.0.1:62001",  # 设备名
#     "appPackage": "com.android.settings",  # 包名
#     "appActivity": "com.android.settings.Settings",  # 应用名
#     "noRest": False  # 不允许重置
# }

info = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "192.168.200.187:5555",
    "appPackage": "com.hongsen.outdoor",
    "appActivity": "com.hongsen.outdoor.activity.MainActivity",
    "noRest": False
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
driver.find_element_by_id('com.hongsen.outdoor:id/tv_exit').click()
time.sleep(2)
driver.find_element_by_id('com.hongsen.outdoor:id/p_img_13').click()
time.sleep(2)
driver.find_element_by_id('com.hongsen.outdoor:id/tv_jq_dl').click()
