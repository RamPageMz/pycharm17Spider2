# -*- coding:utf-8 -*-
# Python file
# Name  :   spider
# Create:   2018/03/18 15:41
# Author:   Ma
# Contact   1033516561@qq.com

# Quote :   

# Begin

import string
import urllib.request
import datetime
import requests


# http://movie.douban.com/
# http://www.dytt8.net/

# from the web url to get movie list we can visit
def get_movie_url():
    start_time = datetime.datetime.now()

    search_url = "http://www.dytt8.net/"
    content = urllib.request.urlopen(search_url).read()  # get all html data
    movie_start = 0
    count_film = 0
    # print(content)
    movie_list = []

    while count_film < 120:
        movie_start = content.find(('/html/gndy').encode(), movie_start + 1)
        url_get = content[movie_start:movie_start + 35]
        url_get = str(url_get)
        # print(url_get)

        if url_get[20] in string.digits:  # no.21 in matrix not digits mean invalid
            count_film += 1
            print(count_film, '\t:\t', url_get)
            movie_list.append(
                'http://www.dytt8.net' + url_get[2:-1])  # for there is b' before and ' behind so cut the top and tail
        else:
            print("invalid!!!  ", url_get)
            continue

    # end while

    end_time = datetime.datetime.now()

    print("^^^^^ get all url time:", ((end_time - start_time).microseconds * 1.0) / 1000000)

    print("*************")
    print("show movie_list")
    print("*************")
    print(movie_list)
    print(len(movie_list))

    print("***************end function**************")

    # for the first and second is a collection of movies so jump them
    return movie_list[2:]


# end get_movie_url


def get_movie_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'}
    req = requests.session()  # req = urllib.request.Request(url, headers=headers)
    req.headers.update(headers)
    r = req.get(url)
    # comment_html = urllib.request.urlopen(req).read()
    # comment_html = str(comment_html, 'gbk')  # 解决编码问题
    return r.content.decode('gbk', 'ignore')
