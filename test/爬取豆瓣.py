# -*-coding:  UTF-8
# @Time    :  2021/9/30 20:21
# @Author  :  Cooper
# @FileName:  爬取豆瓣.py
# @Software:  PyCharm
# encoding: utf-8
'''
  @author 李华鑫
  @create 2020-10-14 8:30
  Mycsdn：https://buwenbuhuo.blog.csdn.net/
  @contact: 459804692@qq.com
  @software: Pycharm
  @file: 豆瓣.py
  @Version：1.0

'''
import requests
from lxml import etree
import csv

# 豆瓣top250网址
doubanUrl = 'https://movie.douban.com/top250?start={}&filter='


# 获取网页源码
def getSource(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    # 以防出现乱码 设置编码格式
    response.encoding = 'utf-8'
    return response.text


# 引言 评分 网址 标题 ---> 网页源代码中
# 获取电影信息
def getEveryItem(source):
    # 生成一个Html对象
    selector = etree.HTML(source)
    # 通过selector对象来找到  电影信息
    movieItemList = selector.xpath('//div[@class="info"]')

    # 定义一个空列表
    movieList = []

    # 通过for循环来遍历
    for eachMovie in movieItemList:
        # 创建一个字典，向列表中存储数据[{电影一},{电影二}...]
        movieDict = {}

        title = eachMovie.xpath('div[@class="hd"]/a/span[@class="title"]/text()')  # 电影名
        otherTitle = eachMovie.xpath('div[@class="hd"]/a/span[@class="other"]/text()')  # 其他名称
        link = eachMovie.xpath('div[@class="hd"]/a/@href')[0]  # 链接
        star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]  # 评分
        quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')  # 引言

        # 条件语句：如果有引言则写引言，若没有则不写
        if quote:
            quote = quote[0]
        else:
            quote = ''

        # 保存数据
        movieDict['title'] = ''.join(title + otherTitle)
        movieDict['url'] = link
        movieDict['star'] = star
        movieDict['quote'] = quote
        print(movieDict)

        movieList.append(movieDict)

    return movieList


# 保存数据
def writeData(movieList):
    with open('douban_top250.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'star', 'quote', 'url'])
        writer.writeheader()  # 写入表头
        for each in movieList:
            # 逐行写入
            writer.writerow(each)


# 启动
if __name__ == "__main__":
    movieList = []
    for j in range(100):

        # 一共10页，循环10次
        for i in range(10):
            # 获取url
            pageLink = doubanUrl.format(i * 25)
            print(pageLink)
            source = getSource(pageLink)
            movieList += getEveryItem(source)

    # writeData(movieList)
