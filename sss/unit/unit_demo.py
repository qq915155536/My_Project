#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/5 10:46
# Author :A0025-江苏-小丹
# QQ:915155536
# File :unit_demo.py
#  ===========================
import unittest

class UnitDemo(unittest.TestCase):
    #类前置条件（整个类中，只运行一次）
    @classmethod
    def setUpClass(cls) -> None:
        print('这是类前置>>>')
    #类后置条件（整个类中，只运行一次）
    @classmethod
    def tearDownClass(cls) -> None:
        print('这是类后置>>>')

    #前置条件（每条用例启动前都要首先运行setup）
    def setUp(self) -> None:
        print('这是前置条件')
    #后置条件（每条用例执行后都要运行teardown）
    def tearDown(self) -> None:
        print('这是后置条件')


    #测试用例1
    def test_01(self):
        print('这是test_01')

    #测试用例2
    def test_02(self):
        print('这是test_02')

    #测试用例3
    def test_03(self):
        print('这是test_03')

    #普通函数
    def sum(self):
        print('这是普通函数！')

if __name__ == '__main__':
    #unittest框架运行方式1
    unittest.main()