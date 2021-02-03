#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/3 10:10
# Author :A0025-江苏-小丹
# QQ:915155536
# File :1.py
#  ===========================
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 登录网址
my_browser = webdriver.Chrome()
my_browser.implicitly_wait(10)
my_browser.get('http://39.98.138.157/shopxo/index.php')
my_browser.maximize_window()

el = my_browser.find_element_by_id("ai-topsearch")
print(el.get_attribute('value'))

js="document.getElementById('ai-topsearch').setAttribute('value','测试')"

my_browser.execute_script(js)

js1="arguments[0].innerHTML='hahahahaha'"

my_browser.execute_script(js1,el)
print(el.text)
