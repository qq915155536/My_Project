#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/3 9:17
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_log.py
#  ===========================

import os
import logging
def my_log(log_name):
    #创建日志器
    logger=logging.getLogger(log_name)
    #设置日志级别
    logger.setLevel(logging.DEBUG)
    #创建处理器1(终端)
    if not logger.handlers:
        sh=logging.StreamHandler()
        #创建处理器2（文件）
        #获取当前文件目录
        # base_dir=os.path.abspath(os.path.dirname(__file__))
        # #拼接日志文件存放路径
        # path=os.path.join(base_dir,f'log\\{log_name}.log')
        # fh=logging.FileHandler(path,encoding='utf-8')
        #创建格式器
        """
        1) %(asctime)s	  发生的时间
        2) %(levelname)s  日志级别
        3) %(filename)s	  文件名
        4) %(lineno)d	  所在的行号
        5) %(message)s	  日志内容
        
        """
        fmt='%(asctime)s — [%(levelname)s] <%(filename)s> — 第%(lineno)d行：%(message)s'
        formater=logging.Formatter(fmt=fmt)

        #为处理器添加格式器
        sh.setFormatter(formater)
        # fh.setFormatter(formater)

        #为日志器添加处理器
        logger.addHandler(sh)
        # logger.addHandler(fh)
    return logger

if __name__ == '__main__':
    logger=my_log('my_log')
    logger.debug('这是debug')
    logger.info('这是info')
    logger.warning('这是warning')
    logger.error('这是error')
    logger.critical('这是critical')





















