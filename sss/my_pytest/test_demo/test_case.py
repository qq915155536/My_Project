#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/22 9:55
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test_case.py
#  ===========================
import pytest


# 前置与后置条件

def setup_function():
    print('setup_function')


def teardown_function():
    print('teardown_function')


# 模块前置与后置
def setup_module():
    print('setup_module')


def teardown_module():
    print('teardown_module')


# 测试用例
def test_02():
    print('test_02')


def test_01(func_01):
    """
    :param func_01: conftest中的预置函数
    """
    print('test_01')


class TestDemo:
    """
    1.pytest中class类，以Test开头
    2.class中前后置函数的运行顺序等级：
    setup_class
    setup_method
    setup
    teardown
    teardown_method
    teardown_class
    """
    def setup(self):
        print('这是类中的setup')

    def teardown(self):
        print('这是类中的teardown')

    def setup_class(self):
        print('这是setup_class')

    def teardown_class(self):
        print('这是teardown_class')

    def setup_method(self):
        print('这是setup_method')

    def teardown_method(self):
        print('这是teardown_method')

    def test_c01(self):
        print('这是类中的test_c01')

    def test_c02(self):
        print('这是类中的test_c02')


# pytest运行主入口
if __name__ == '__main__':
    # -s ，显示用例执行内容 ；
    # test_case.py::test_01 ，指定只执行当前目录下的test_case.py文件中的test_01用例
    # -v，显示详细信息，用例是否通过等
    # -rA，用于测试结果的简单统计
    # pytest.main(['-s', 'test_case.py::test_01', '-v', '-rA'])
    pytest.main(['-s', 'test_case.py', '-rA'])
