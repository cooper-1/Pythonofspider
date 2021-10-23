# -*-coding:  UTF-8
# @Time    :  2021/10/17 9:14
# @Author  :  Cooper
# @FileName:  6.2获取动态加载的数据.py
# @Software:  PyCharm
from requests_html import HTMLSession  # 导入HTMLSession类
from fake_useragent import UserAgent
import os

i = 0
location = os.getcwd() + '/fake_useragent_0.1.11.json'
header = {'Useragent': UserAgent(path=location).random}
session = HTMLSession()  # 创建HTML会话对象

# 发送网洛请求
r = session.get('https://movie.douban.com/tag/#/?sort=U&range=0,10'
                '&tags=%E7%94%B5%E5%BD%B1,2020', headers=header)
r.encoding = 'gb2312'  # 编码
if r.status_code == 200:  # 判断请求是否成功
    r.html.render()  # 调用render()方法，没有Chromium浏览器就自动下载
    class_wp = r.html.xpath('.//div[@class="list-wp"]/a')  # 获取当前页面中所有电影信息的a标签
    for a in class_wp:
        title = a.find('p span')[0].text  # 获取电影名称
        rate = a.find('p span')[1].text  # 获取电影评分
        details_url = a.attrs.get('href')  # 获取详情页url地址
        img_url = a.find('img')[0].attrs.get('src')  # 获取图片url地址
        print('电影名称为：', title)  # 打印电影名称
        print('电影评分为：', rate)  # 打印电影评分
        print('详情页地址为：', details_url)  # 打印电影详情页url地址
        print('图片地址为：', img_url)  # 打印电影图片地址
