#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/10/25 11:54
# Author :A0025-江苏-小丹
# QQ:915155536
# File :login_logout.py
#  ===========================
from sss.Api.base_api import WebApi

# 目标信息
browser_type='Chrome'
url='http://192.168.250.47/kss-js/#/login'

#谷歌浏览器访问目标地址
js_browser=WebApi(browser_type)
js_browser.visit_url(url)


# 登录方法
def login(user,password):
    #输入用户名和密码，点击登录
    js_browser.my_send_keys('xpath','//input[@placeholder="请输入用户名"]',user)
    js_browser.my_send_keys('xpath','//input[@placeholder="请输入密码"]',password)
    js_browser.my_click('xpath','//button')

def logout():
    js_browser.my_click('xpath','//span[text()="退出"]')
    js_browser.my_click('xpath','//div[@class="el-message-box__btns"]/button[2]')

# 测试专用
if __name__ == '__main__':
    login('admin','111111')
    logout()




