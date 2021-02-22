#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/22 11:14
# Author :A0025-江苏-小丹
# QQ:915155536
# File :conftest.py
#  ===========================
"""
1.这是pytest中setup和teardown的配置文件
2.这是pytest中的预置函数定义的配置文件
2.配置文件必须命名为conftest.py
3.scope参数定义的四种等级,默认等级为function：
    session：在本次session级别中只执行一次
    module：在模块级别只执行一次
    class：在类级别中只执行一次
    function：在函数级别执行一次
"""
import pytest



@pytest.fixture(scope='function')
def func_01():
    print('这里是func_01')
