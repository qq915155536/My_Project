from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

driver.implicitly_wait(10)
driver.maximize_window()

#访问目标网站
driver.get('http://192.168.200.234/js-jls/#/login')

#登录系统
driver.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys('admin')
driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('111111')
driver.find_element_by_xpath('//span[text()="登录"]').click()

#进入警情联动—警情信息
driver.find_element_by_xpath('//span[text()="警情联动"]').click()
driver.find_element_by_xpath('//span[text()="警情信息"]').click()

#警情登记
driver.find_element_by_xpath('//span[text()="警情登记"]').click()
#信息完善
driver.find_element_by_xpath('//input[@placeholder="请选择警情大类"]').click()
driver.find_element_by_xpath('//span[text()="测试动态指数"]').click()









driver.find_element_by_xpath('//span[text()="保存"]').click()

sleep(5)
#退出浏览器


# //span[text()="系统管理"]

