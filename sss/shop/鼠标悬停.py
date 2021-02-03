from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

d = webdriver.Chrome()
d.implicitly_wait(10)
d.maximize_window()
d.get('http://www.baidu.com')
e1 = d.find_element_by_xpath('//*[@id="s-usersetting-top"]')

#生成对象，传入driver
action=ActionChains(d)
#传入要悬停的元素
action.move_to_element(e1).perform()

