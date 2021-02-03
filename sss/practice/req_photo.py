#  ===========================
# -*- coding:utf-8 -*-
# Time :2020/11/19 16:03
# Author :A0025-江苏-小丹
# QQ:915155536
# File :dem3.py
#  ===========================
import requests
import parsel
#网址编号
url_num_list=[227,225,224,220,218,217,199,198,195,193,191,189,186,184]
#拼接网址
for num in url_num_list:
    base_url=f'http://yxcq.qq.com/webplat/info/news_version3/6960/17087/17089/m12508/201509/381{num}.shtml'
    # print(base_url)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    #发送请求
    res=requests.get(url=base_url,headers=headers)
    # res.encoding=res.apparent_encoding
    res.encoding='gbk'   #指定网址的编码（和原网址编码保持一致）
    res1=parsel.Selector(res.text)
    #获取英雄名字
    name= res1.xpath('//div[@class="w_xinxi"]/h2/text()').extract_first()
    #获取图片
    photo=res1.xpath('//div[@class="w_bodybg"]/@style').extract_first()
    l=photo.split('/')[-1].split(')')[0]   #l为图片最后的名字 1436515869668.jpg
    #拼接图片url
    photo_url='http://ossweb-img.qq.com/upload/webplat/info/yxcq/20150924/'+l

    photo_data=requests.get(photo_url,headers=headers).content

    #保存数据
    photo_name='E:\\My_Project\\sss\\practice\\photo\\'+f'{name}.jpg'

    with open(photo_name, 'wb')as f:
        print('正在保存图片：',name)
        f.write(photo_data)



