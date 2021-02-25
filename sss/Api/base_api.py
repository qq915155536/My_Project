#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/10/25 9:14
# Author :A0025-江苏-小丹
# QQ:915155536
# File :base_api.py
#  ===========================
from selenium import webdriver
import time
from sss.Api.ChromeOptions import Options
from selenium.webdriver.support.wait import WebDriverWait


def open_browser(browser_type):
    """
    构造浏览器
    :param browser_type:浏览器类型，如‘Chrome’
    :return: 返回一个浏览器对象 driver
    """
    options = Options().options_conf()
    try:
        driver = getattr(webdriver, browser_type)(options=options)
        driver.implicitly_wait(10)
    except BaseException as e:
        print(f'您输入的浏览器不存在，已为您启动谷歌浏览器！,信息为:<{e}>')
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
    return driver


class WebApi:
    """
    这是webui关键字驱动类，生成浏览器对象
    """

    # 初始化浏览器
    def __init__(self, browser_type):
        self.driver = open_browser(browser_type)

    # 浏览器访问目标网址
    def visit_url(self, url):
        self.driver.get(url)

    def my_location(self, location_type, location_content):
        """
        元素定位方法
        :param location_type: 元素定位方式
        :param location_content: 元素定位内容
        :return: 一个元素对象
        """
        try:
            return self.driver.find_element(location_type, location_content)
        except BaseException as e:
            print(e)

    # 点击方法
    def my_click(self, location_type, location_content):
        self.my_location(location_type, location_content).click()

    # 输入方法
    def my_send_keys(self, location_type, location_content, text):
        self.my_location(location_type, location_content).send_keys(text)

    # 清除方法
    def my_clear(self, location_type, location_content):
        self.my_location(location_type, location_content).clear()

    # 强制等待方法
    def my_wait(self, s):
        time.sleep(s)

    # 显示等待方法
    def assert_wait(self, location_type, location_content):
        try:
            return WebDriverWait(self.driver, 5, 0.2).until(
                lambda e1: self.my_location(location_type, location_content),
                message='显示等待没有发现此元素')
        except:
            return False

    def my_assert(self, location_type, location_content, expect_result):
        """
        断言方法：获取元素的文本值和预期结果比对
        :param expect_result:预期结果
        """
        value = self.my_location(location_type, location_content).text
        if value == expect_result:
            return True
        else:
            return False

    def my_handle(self):
        # 切换句柄(进入商品详情页)
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 浏览器退出
    def my_quit_browser(self):
        self.driver.quit()


# 调试专用
if __name__ == '__main__':
    my_browser = WebApi('Chrome')
    url = 'http://www.baidu.com'
    my_browser.visit_url(url)
    my_browser.my_send_keys('id', 'kw', '测试')
    my_browser.my_click('id', 'su')
    my_browser.my_wait(3)
    res = my_browser.my_assert('xpath', '//div[@class="search_tool"]', '搜索工具')
    if res:
        print('执行成功!')
        my_browser.my_quit_browser()
    else:
        print('执行失败！')
