#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/1/21 16:51
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo1.py
#  ===========================
import configparser

#读取配置项内容
def read_ini(path,title,key):
    """
    :param path: 配置文件名
    :param title: 配置项
    :param key: 配置名
    :return: 配置值
    """
    my_conf=configparser.ConfigParser()
    my_conf.read(path)
    url=my_conf.get(title,key)
    return url

if __name__ == '__main__':
    print(read_ini('./config.ini', 'TEST_SERVER', 'url'))



