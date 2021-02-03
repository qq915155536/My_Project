#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/12 18:09
# Author :A0025-江苏-小丹
# QQ:915155536
# File :login.py
#  ===========================
from sss.Api.base_api import WebApi
gx_browser=WebApi('Chrome')
gx_browser.visit_url('http://192.168.250.47/team-gx-test/#/login')
gx_browser.my_send_keys('xpath','//input[@placeholder="请输入用户名"]','admin')
gx_browser.my_send_keys('xpath','//input[@placeholder="请输入密码"]','111111')
gx_browser.my_click('xpath','//span[text()="登录"]')
print('hahah')