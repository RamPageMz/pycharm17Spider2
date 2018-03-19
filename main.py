# -*- coding:utf-8 -*-
# Python file
# Name  :   main
# Create:   2018/03/18 16:03
# Author:   Ma
# Contact   1033516561@qq.com

# Quote :   

# Begin

import spider
import datetime
import re
import binascii

movie_list = spider.get_movie_url()

for one in movie_list:
    try:
        content = spider.get_movie_html(one)
    except UnicodeDecodeError:
        print("GBK 解码出错！！！")
        continue

    # print("content: ", content)
    aa = content.find(('href="magnet:?'), 1)

    link = re.findall(('magnet:?([\S]*)"><strong>'), content, re.S | re.I)
    if len(link) == 0:
        print("没找到link信息")
    else:
        link1 = str(link[0])
        link1 = "magnet:" + link1[2:-1]
        print(link1)  # 成功获得有效的磁力链接 复制打开迅雷即可下载种子

    name = re.findall(('<h1><font color=#07519a>([\S]*)</font></h1>'), content, re.S | re.I)
    # name = re.findall(('www.ygdy8.com.([\S]*).mkv">'), content, re.S | re.I)
    if len(name)==0:
        print("没找到片名信息")
    else:
        name1 = str(name[0])
        nn = name1[2:-1]
        print("name", name1)  # 此时获得的是正确内容的错误编码的信息
        print("-------------------------")

