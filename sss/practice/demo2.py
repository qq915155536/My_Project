#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/10/30 17:02
# Author :A0025-江苏-小丹
# QQ:915155536
# File :demo2.py
#  ===========================
import mysql.connector
host='192.168.200.200'
port='3306'
user='root'
pwd='123456'
db='test'

con1=mysql.connector.connect(host=host,
                             port=port,
                             user=user,
                             password=pwd,
                             database=db,
                             auth_plugin='mysql_native_password'
                             )

cur1=con1.cursor()    #获取游标
cur1.execute('show databases')#游标执行sql语句

# for x in cur1:
#     print(x)

# res1=cur1.fetchall()
# res1=cur1.fetchone()
res1=cur1.fetchmany(3)
print(res1)

