# -*-coding:  UTF-8
# @Time    :  2021/10/6 19:25
# @Author  :  Cooper
# @FileName:  爬取即时新闻.py
# @Software:  PyCharm
from agency.requ2 import getlist
import re

response = getlist('http://news.youth.cn/jsxw/index.htm')
# print(response.content.decode('gb2312'))
title = response.html.xpath('//ul[@ class="tj3_1"]/li/a/text()')
times = response.html.xpath('//ul[@ class="tj3_1"]/li/font/text()')
href = response.html.xpath('//ul[@ class="tj3_1"]/li/a/@href')
# print(title)
# print(times)
# print(href)
# print(len(title))
# print(len(times))
# print(len(href))
for i, j in enumerate(title):
    print(i + 1, '新闻的标题为：', j, end='\t')
    print('新闻的url为：', 'http://news.youth.cn/jsxw/' + href[i], end='\t')
    print('新闻发布的时间为：', times[i])

# for li in response.html.find('li', containing='疫情'):
for li in response.html.find(".tj3_1 >li"):  # 使用的是css选择器
    print(li)
    print(li.find('a')[0].text)
