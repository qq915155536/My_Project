#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/13 9:16
# Author :A0025-江苏-小丹
# QQ:915155536
# File :unit_ddt.py
#  ===========================
from ddt import ddt, data, unpack, file_data
import unittest


@ddt
class Demo(unittest.TestCase):

    # 1）一条数据，通过data传值给函数参数
    # @data('测试1')
    # def test_01(self, txt):
    #     print(txt)

    # 2）多条数据，分批传入，通过data传值，传入的内容，基于逗号分割，每一次传一个值进去,生成两条用例。
    # @data('测试1', '测试2')
    # def test_02(self, txt):
    #     print(txt)

    #3）多条数据，一次性传入，故只有一个用例通过data传值（一个列表），再通过unpack解析成单个，
    # @data(['admin','123456'])
    # @unpack
    # def test_03(self, username,password):
    #     print(username)
    #     print(password)

    #4)多条数据，一次性传入，故只有一个用例通过data传值（一个列表），再用一个参数去接收列表，按索引取值。
    # @data(['admin','123456'])
    # def test_04(self,args):
    #     print(args,type(args))     #agrs=['admin','123456']
    #     print(args[0])
    #     print(args[1])

    #5)多组多条数据，两次传入，有两个用例，每次传入的都是逗号分割的一个列表
    # @data(['admin','123456'],['ceshi','111111'])
    # def test_05(self,args):
    #     print(args,type(args))
    #     print(args[0])
    #     print(args[1])

    @data(['admin','123456'],['ceshi','111111'])
    def test_05(self,args):
        print(args,type(args))
        print(args[0])
        print(args[1])

if __name__ == '__main__':
    unittest.main()
