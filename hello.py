# Python file
# Name  :   hello
# Create:   2018/03/18 15:40
# Author:   Ma
# Contact   1033516561@qq.com

# Quote :   

# Begin

import sys
import urllib.request

print("Hello!")
print("编码：", sys.getdefaultencoding())

name = "小明"
print(name)
print(name.encode('utf-8'))

name1 = name.encode('utf-8')
print(name1)

print(name1.decode('utf-8'))

# print('\xE5\x85\x84\xE5\xBC\x9F\xE9\x9A\xBE\xE5\xBD\x93 \xE6\x9D\x9C\xE6\xAD\x8C'.decode('utf-8'))

# \xbf\xe7\xb4\xce\xd4\xaa\xc9\xd9\xc5\xae\xb4\xf3\xd7\xf7\xd5\xbd.HD.720p.\xb9\xfa\xd3\xef\xd6\xd0\xd7\xd6
# b'\xbf\xe7\xb4\xce\xd4\xaa\xc9\xd9\xc5\xae\xb4\xf3\xd7\xf7\xd5\xbd.HD.720p.\xb9\xfa\xd3\xef\xd6\xd0\xd7\xd6'

response = urllib.request.urlopen('http://www.dytt8.net/html/gndy/jddy/20180318/56528.html')
html = str(response.read(), 'gbk')
print(html)     # 成功

