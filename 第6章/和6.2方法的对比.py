# -*-coding:  UTF-8
# @Time    :  2021/10/17 9:26
# @Author  :  Cooper
# @FileName:  和6.2方法的对比.py
# @Software:  PyCharm
from agency.requ2 import getlist
import jsonpath
import json

url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&year_range=2020,2020'
response = getlist(url)
print(response.content.decode('utf-8'))
print('-' * 50)
jsonobj = json.loads(response.content)
# 导演
daoyan = jsonpath.jsonpath(jsonobj, '$..directors')
print(daoyan)
# 评分
rate = jsonpath.jsonpath(jsonobj, '$..rate')
print(rate)
# 封面地址
cover = jsonpath.jsonpath(jsonobj, '$..cover')
print(cover)
# 详情页地址
xqurl = jsonpath.jsonpath(jsonobj, '$..url')
print(xqurl)
# 电影名
title = jsonpath.jsonpath(jsonobj, '$..title')
print(title)
# 演员阵容
casts = jsonpath.jsonpath(jsonobj, '$..casts')
print(casts)
print('排名 电影名称 评分 详情页地址 图片地址')
for i, j in enumerate(title):
    print(i + 1, '\t', j, '\t', rate[i], '\t', xqurl[i], cover[i])
    # print(i + 1, '\t', j)
