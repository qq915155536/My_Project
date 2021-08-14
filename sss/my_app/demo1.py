#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/4/11 18:31
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo1.py
#  ===========================
from appium import webdriver

info={
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    #包名
    "appPackage": "com.android.settings",
    #应用名
    "appActivity": "com.android.settings.Settings",
    #禁止重置
    "noRest": False
}

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',info)
#进入设置，点击搜索
driver.find_element_by_id('com.android.settings:id/search').click()
#搜素框内输入蓝牙
driver.find_element_by_id('android:id/search_src_text').send_keys('蓝牙')
#点击返回箭头
driver.find_element_by_xpath('//*[@content-desc="收起"]').click()

#获取放大镜的相关信息：
search_button=driver.find_element_by_id('com.android.settings:id/search')
#位置、横、纵坐标
print(search_button.location)
print(search_button.location['x'])
print(search_button.location['y'])
#大小
print(search_button.size)
print(search_button.size['height'])
print(search_button.size['width'])
