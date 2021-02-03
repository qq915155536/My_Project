#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/14 15:24
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo1.py
#  ===========================
import threading
from selenium import webdriver

driver1=webdriver.Chrome()
driver2=webdriver.Chrome()
driver3=webdriver.Chrome()

def visit(driver):
    driver.get('http://www.baidu.com')



l=[]
l.append(threading.Thread(target=visit,args=[driver1]))
l.append(threading.Thread(target=visit,args=[driver2]))
l.append(threading.Thread(target=visit,args=[driver3]))
for i in l:
    i.start()
