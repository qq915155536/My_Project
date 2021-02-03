from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

#访问目标网站
driver.get('http://192.168.250.47/kss-js/#/login')

#登录系统
driver.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys('admin')
driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys('111111')
driver.find_element_by_xpath('//span[text()="登录"]').click()


#警务公开——新增社会关系功能
#进入新增社会关系页面
driver.find_element_by_xpath('//span[text()="后台管理"]').click()
driver.find_element_by_xpath('//span[text()="警务公开"]').click()
driver.find_element_by_xpath('//span[text()="新增社会关系"]').click()
#输入数据，点击确认
driver.find_element_by_xpath('//input[@placeholder="请输入人员名称"]').send_keys('李飞')
driver.find_element_by_xpath('//li[@value-key="李飞"]').click()
driver.find_element_by_xpath('//input[@placeholder="请输入家属姓名"]').send_keys('李大飞')
driver.find_element_by_xpath('//input[@placeholder="请输入家属身份证号"]').send_keys('320321199302191000')
driver.find_element_by_xpath('//input[@placeholder="请输入家属家属联系方式"]').send_keys('15158801000')
driver.find_element_by_xpath('//input[@placeholder="请选择与在押人关系"]').click()
sleep(1)
driver.find_element_by_xpath('//span[text()="合伙人"]').click()
driver.find_element_by_xpath('//input[@maxlength="100"]').send_keys('浙江省杭州市')
driver.find_element_by_xpath('//span[text()="确认"]').click()








# driver.quit()

