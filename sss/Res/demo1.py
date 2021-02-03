#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/21 17:12
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo1.py
#  ===========================
import unittest
from ddt import ddt, file_data
from sss.conf.my_read import read_ini


@ddt
class Res_Api(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url = read_ini('../conf/config.ini', 'TEST_SERVER', 'url')

    @file_data('../conf/data.yaml')
    def test_01(self, path):
        url = self.url + path
        print(url)

    def test_02(self):
        pass


if __name__ == '__main__':
    unittest.main()
