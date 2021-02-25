#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/25 13:58
# Author :A0025-江苏-小丹
# QQ:915155536
# File :ChromeOptions.py
#  ===========================
import time

from selenium import webdriver


class Options:
    """这是谷歌浏览器配置类"""

    def options_conf(self):
        # 创建配置对象options
        options = webdriver.ChromeOptions()
        # 去掉默认的自动化提示
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 窗体最大化
        options.add_argument('start-maximized')

        # 无头模式:无界面运行
        # options.add_argument('--headless')

        # 指定窗口大小
        # options.add_argument('--window-size=400,400')

        # 加载本地缓存
        """
        1.通过指令查找本地缓存：chrom：//version
        2.传入缓存 : --user-data-dir=
        3.调用缓存时，要关闭其他浏览器
        """
        # options.add_argument(r'--user-data-dir=C:\Users\ADMINI~1\AppData\Local\Temp\scoped_dir7136_268498814')

        # 添加配置去掉密码管理弹窗（是否保存、更新密码）
        prefs={}
        prefs['credentials_enable_service']=False
        prefs['profile.password_manager_enabled']=False
        options.add_experimental_option('prefs',prefs)

        # 隐身模式
        # options.add_argument('incognito')

        return options


if __name__ == '__main__':
    # 生成配置
    options = Options().options_conf()
    d = webdriver.Chrome(options=options)
    d.get('http://192.168.250.47/team-gx-test/#/login')
    d.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys('admin')
    d.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('111111')
    d.find_element_by_xpath('//span[text()="登录"]').click()

    #截图
    time.sleep(20)
    d.save_screenshot('./1.png')
    d.quit()