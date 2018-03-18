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

# for one in movie_list:
content = spider.get_movie_html(movie_list[0])
# print(content)
aa = content.find(('href="magnet:?').encode(), 1)
# print(content[aa:aa + 100])

link = re.findall(('magnet:?([\S]*)"><strong>').encode(), content, re.S | re.I)
link1 = str(link[0])
# print("link", link1)
link1 = "magnet:" + link1[2:-1]
print(link1)  # 成功获得有效的磁力链接 复制打开迅雷即可下载种子

name = re.findall(('www.ygdy8.com.([\S]*).mkv">').encode(), content, re.S | re.I)
name1 = str(name[0])
nn = name1[2:-1]
print("name", nn)  # 此时获得的是正确内容的错误编码的信息 \x
# print("nn", name[0].decode('utf-8)'))
