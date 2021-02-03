#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/14 8:53
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo1.py
#  ===========================
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 登录网址
my_browser = webdriver.Chrome()
my_browser.implicitly_wait(10)
my_browser.get('http://39.98.138.157/shopxo/index.php')
my_browser.maximize_window()

# 登录账号
my_browser.find_element_by_link_text('登录').click()
my_browser.find_element_by_name('accounts').send_keys('qq915155536')
my_browser.find_element_by_name('pwd').send_keys('qq915155536')
my_browser.find_element_by_xpath('//button[text()="登录"]').click()
# 显示等待判断是否登录成功
WebDriverWait(my_browser, 5, 0.2).until(lambda e1: my_browser.find_element_by_link_text('退出'), message='登录失败！')

# 搜索商品
my_browser.find_element_by_id('search-input').send_keys('手机')
my_browser.find_element_by_id('ai-topsearch').click()
my_browser.find_element_by_xpath('//p[contains(@title,"苹果")]').click()
# 切换句柄(进入商品详情页)
handles = my_browser.window_handles
my_browser.close()
my_browser.switch_to.window(handles[1])

# 选择商品属性，加入购物车
my_browser.find_element_by_xpath('//li[@data-value="套餐二"]').click()
my_browser.find_element_by_xpath('//li[@data-value="银色"]').click()
my_browser.find_element_by_xpath('//li[@data-value="64G"]').click()
my_browser.find_element_by_xpath('//input[@type="number"]').clear()
my_browser.find_element_by_xpath('//input[@type="number"]').send_keys('2')
my_browser.find_element_by_xpath('//button[@title="加入购物车"]').click()

##显示等待判断是否加入成功（断言‘加入成功’弹窗）
WebDriverWait(my_browser, 5, 0.2).until(lambda e1: my_browser.find_element_by_xpath('//p[text()="加入成功"]'),
                                        message='加入购物车失败！')

# 进入购物车添加断言查看商品是否存在
my_browser.find_element_by_xpath('//span[text()="购物车"]').click()
text1 = '套餐：套餐二'
text2 = my_browser.find_element_by_xpath('//ul[@class="goods-attr"]/li').text
assert text1 == text2, '商品不存在！'

print('自动加入购物车成功！！！')
my_browser.quit()
