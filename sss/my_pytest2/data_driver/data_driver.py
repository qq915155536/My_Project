#  ===========================
# -*- coding:utf-8 -*-
# Time :2021/2/23 10:41
# Author :A0025-江苏-小丹
# QQ:915155536
# File :data_driver.py
#  ===========================
import yaml

def read_yaml(path):
    """
    :param path:要读取的yaml文件路径
    :return:   yaml数据
    """
    with open(path,'r',encoding='utf-8') as f:
        data=yaml.load(f,Loader=yaml.FullLoader)
    return data

if __name__ == '__main__':
    print(read_yaml('./data.yaml'))