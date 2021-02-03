#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/12 15:31
# Author :A0025-江苏-小丹
# QQ:915155536
# File :suite_demo.py
#  ===========================
import unittest
import os
from HTMLTestReportCN import HTMLTestRunner
from sss.unit.unit_demo1 import Unit_Demo

# 创建套件
suite = unittest.TestSuite()

# 添加用例到套件
# （单个添加）
# suite.addTest(Unit_Demo('test_03'))
# suite.addTest(Unit_Demo('test_01'))

# （批量添加,直接添加一个类）
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Unit_Demo))

##（批量添加,按文件名）
# case_dir='./'
# dicover=unittest.defaultTestLoader.discover(start_dir=case_dir,pattern='unit*.py')

# 运行套件，需要有运行器，用例执行顺序为添加用例到套件的顺序
# runner = unittest.TextTestRunner()
# runner.run(suite)
# runner.run(dicover)

# HtmlTestRunner报告
#保存路径：
report_path='./report/'
#报告名称
report_file=report_path+'report.html'

if not os.path.exists(report_path):
    os.mkdir(report_path)
with open(report_file,'wb')as f:
    runner=HTMLTestRunner(stream=f,title='这是第一份测试报告',description='这是测试描述',tester='测试人1')
    runner.run(suite)
