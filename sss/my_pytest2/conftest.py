#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/23 14:47
# Author :A0025-江苏-小丹
# QQ:915155536
# File :conftest.py
#  ===========================
import pytest
import requests

#预置函数获取接口关联所需的token
@pytest.fixture()
def get_token():
    url='http://39.98.138.157:5000/api/login'
    data={'username':'admin','password':'123456'}
    res=requests.post(url=url,json=data)
    print(res.text)
    token=res.json()['token']
    return token