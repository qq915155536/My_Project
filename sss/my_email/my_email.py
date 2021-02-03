#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/7 9:11
# Author :A0025-江苏-小丹
# QQ:915155536
# File :my_email.py
#  ===========================
import smtplib
#导入邮件文本模块
from email.mime.text import MIMEText
#导入邮件头部模块
from email.header import Header
#导入邮件附件模块
from email.mime.multipart import MIMEMultipart
#导入邮件图片模块
from email.mime.image import MIMEImage


#smtp:是一种简单的邮件传输协议，创建邮箱服务器连接 smtplib.SMTP_SSL(邮箱连接地址,端口号)smtp.xx.com  端口号  ssl  465 587  邮局
# 邮箱163:smtp.163.com
# qq邮箱:smtp.qq.com
my_smtp=smtplib.SMTP_SSL('smtp.qq.com','465')

# 163的用户名和密码,直接填写就行.如果说是qq的邮箱 用户名邮箱号,密码,授权码 设置 --账户--开启POP3/SMTP服务--点击授权码
sender='915155536@qq.com'
receiver=['915155536@qq.com']   #接收人可多个，用列表存放
my_smtp.login(sender,'ehiumfoqatblbfjc')

#设置邮件内容 （文本）
text='只是测试而已——正文噢！'
meg=MIMEText(_text=text,_subtype='plain',_charset='utf-8')  # _subtype 文件类型  文本  html  base64(二进制类型)  plain默认就是纯文本

#设置邮件内容（html）
# html='''
#     <!doctype html><!--声明当前文档类型-->
#     <html><!--网页结构的开始--->
# 	<head><!--描述网页基本信息-->
# 		<meta charset="UTF-8"><!--声明网页编码格式-->
# 		<title>测试html</title>
# 	</head>
# 	<body><!--可视区域-->
# 		<p>html主题</p>
# 		<h1>标题标签</h1>
# 		<input maxlength='100'></input>
# 		<button>百度一下</button>
#
# 	</body>
# </html>
# '''
#meg=MIMEText(_text=html,_subtype='html',_charset='utf-8')

#设置邮件内容（附件）
# meg=MIMEMultipart()
# with open('1.txt','rb')as f:
#     content=f.read()       #读取附件内容
# fj=MIMEText(content,'base64','utf-8')#写入附件
# fj['Content-Disposition']='attachment;filename="fj.txt"'#添加附件标题
# meg.attach(fj)#把附件添加到邮件中

#设置邮件内容（图片）
# meg=MIMEMultipart()
# with open('1.jpg','rb')as f:
#     content=f.read()
# img=MIMEImage(content)
# img['Content-Disposition']='attachment;filename="1.jpg"'
# meg.attach(img)

#设置邮件头部信息（主题、收、发件人等）
meg['subject']=Header('这是一封测试邮件—主题','utf-8')
meg['From']=Header('测试—发件人','utf-8')
meg['To']=Header('测试—收件人','utf-8')

#邮件服务器发送邮件
my_smtp.sendmail(sender,receiver,meg.as_string())
#退出邮件服务器
my_smtp.quit()
