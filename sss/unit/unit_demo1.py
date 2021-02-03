#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/12 15:23
# Author :A0025-江苏-小丹
# QQ:915155536
# File :unit_demo1.py
#  ===========================
import unittest

class Unit_Demo(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_01(self):
        print('test01')

    def test_02(self):
        print('test02')

    def test_03(self):
        a=1/0
        print('test03')

if __name__ == '__main__':
    unittest.main()