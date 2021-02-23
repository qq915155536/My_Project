#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/23 10:07
# Author :A0025-江苏-小丹
# QQ:915155536
# File :test_case.py
#  ===========================
import pytest
from sss.my_pytest2.data_driver.data_driver import read_yaml


# pytest的数据驱动,直接传递数值
# @pytest.mark.parametrize(['admin','password'],[['张三',1111],['李四',123456],['王五',6666]])
# def test_login(admin, password):
#     print(f'用户名：{admin},密码：{password}')

# pytest的数据驱动,通过函数形式将结果生成并返回。
# @pytest.mark.parametrize('data', read_yaml('./data_driver/data.yaml'))
# def test_login(data):
#     user = data['user']
#     pwd = data['pwd']
#     print(f'用户名：{user},密码：{pwd}')

# 通过设置全局变量实现接口间的关联
# Token=None
# import requests
# @pytest.mark.parametrize('data',read_yaml('./data_driver/login.yaml'))
# def test_login(data):
#     url='http://39.98.138.157:5000/api/login'
#     res=requests.post(url=url,json=data)
#     global Token
#     Token=res.json()['token']
#     print(Token)
#
# def test_02():
#     print(Token)

# 跨模块实现接口关联，可通过预置函数配置文件(conftest.py)实现，把要关联的数据如token写入预置函数文件内，谁需要谁调用
def test_03(get_token):
    print(get_token)


if __name__ == '__main__':
    pytest.main(['-s'])
