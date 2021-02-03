#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/10/25 12:31
# Author :A0025-江苏-小丹
# QQ:915155536
# File :tztg.py
#  ===========================

# 管理员登录系统，创建通知通告
import datetime
from sss.my_log.my_log import my_log
logger=my_log('tztg')
from sss.js.login_logout import *

login('admin','111111')
logger.info('系统登录成功，开始测试>>>')
logger.info('进入通知通告界面ing')
js_browser.my_click('xpath','//span[text()="信息发布"]')
js_browser.my_click('xpath','//span[text()="通知通告"]')
logger.info('进入成功，开始新增测试>>>')
js_browser.my_click('xpath','//span[text()="发布通知"]')

#获取当前时间
t=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')

#生成通知标题
tz_name='测试通知' + t

#传入通知标题
logger.info('输入通知标题>>>')
js_browser.my_send_keys('xpath','//input[@maxlength="25"]',tz_name)

#传入结束时间
logger.info('输入时间>>>')
js_browser.my_send_keys('xpath','//label[text()="结束时间"]/../div/div/input','2020-11-31')

#传入通知内容
logger.info('输入内容>>>')
tz_content='测试内容'+ t
js_browser.my_send_keys('xpath','//textarea',tz_content)

#确认
js_browser.my_click('xpath','//span[text()="确认"]')

logger.info('新增成功！')

js_browser.my_wait(5)

logger.info('测试通过！关闭浏览器！>>>')
#关闭浏览器
js_browser.my_quit_browser()


