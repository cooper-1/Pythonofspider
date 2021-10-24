# -*-coding:  UTF-8
# @Time    :  2021/10/20 22:51
# @Author  :  Cooper
# @FileName:  爬取电影详情页地址.py
# @Software:  PyCharm
from agency.requ2 import getlist
import time
import re
from lxml import etree
from bs4 import BeautifulSoup  # 导入解析html代码的模块
from multiprocessing import Pool  # 导入进程池

start_time = time.time()
detail_urls = []


# detail_urls2 = []


def get(urls):
    # print(urls)
    for url in urls:
        # print(url)
        response = getlist(url)
        # print(response.content.decode('gb2312', errors='ignore'))
        pattern = re.compile('<a href="(.*?)" class="ulink">')
        port = pattern.findall(response.content.decode('gb2312', errors='ignore'))
        # print(port)
        detail_urls.extend(['https://www.ygdy8.net' + i for i in port])
        try:
            for j in detail_urls:
                print(j)
                response_2 = getlist(j)
                html = etree.HTML(response_2.text)
                pattern = re.compile('<a target="_blank" href="(.*?)"><strong><font')
                download_url = pattern.findall(response_2.content.decode('gb2312', errors='ignore'))[0]
                print(download_url)
                name = html.xpath('//div/h1/font/text()')[0]
                print(name)
                html = BeautifulSoup(response_2.text, "html.parser")  # 获取返回的html代码
                # info_all = (html.select('div[id="Zoom"]')[0]).p.text.replace('\u3000', '').split('◎')
                info_all = html.select('div[id="Zoom"]')[0]
                info_all = str(info_all).replace('\u3000', '').replace('<br/>', '').replace('\xa0', '').split('◎')
                # print(info_all)
                date = info_all[8]  # 获取上映时间
                imdb = info_all[9]  # 获取IMDb评分
                douban = info_all[10]  # 获取豆瓣评分
                length = info_all[14]  # 获取片长
                # 电影信息
                info = {'name': name, 'date': date, 'imdb': imdb,
                        'douban': douban, 'length': length, 'download_url': download_url}
                print(info)  # 打印电影信息
        except Exception as e:
            print(e)


class Spider:
    def __init__(self):
        self.detail_urls2 = []

    def get2(self, url):
        response = getlist(url)
        # print(response.content.decode('gb2312', errors='ignore'))
        pattern = re.compile('<a href="(.*?)" class="ulink">')
        port = pattern.findall(response.content.decode('gb2312', errors='ignore'))
        print(port)
        self.detail_urls2.extend(['https://www.ygdy8.net' + i for i in port])
        print('self.detail_urls2', self.detail_urls2)
        try:
            for j in self.detail_urls2:
                print(j)
                response_2 = getlist(j)
                html = etree.HTML(response_2.text)
                pattern = re.compile('<a target="_blank" href="(.*?)"><strong><font')
                download_url = pattern.findall(response_2.content.decode('gb2312', errors='ignore'))[0]
                print(download_url)
                name = html.xpath('//div/h1/font/text()')[0]
                print(name)
                html = BeautifulSoup(response_2.text, "html.parser")  # 获取返回的html代码
                # info_all = (html.select('div[id="Zoom"]')[0]).p.text.replace('\u3000', '').split('◎')
                info_all = html.select('div[id="Zoom"]')[0]
                info_all = str(info_all).replace('\u3000', '').replace('<br/>', '').replace('\xa0', '').split('◎')
                # print(info_all)
                date = info_all[8]  # 获取上映时间
                imdb = info_all[9]  # 获取IMDb评分
                douban = info_all[10]  # 获取豆瓣评分
                length = info_all[14]  # 获取片长
                # 电影信息
                info = {'name': name, 'date': date, 'imdb': imdb,
                        'douban': douban, 'length': length, 'download_url': download_url}
                print(info)  # 打印电影信息
        except Exception as e:
            print(e)


if __name__ == '__main__':
    urls = ['https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'.format(str(i)) for i in range(1, 11)]
    print('\u3000')
    start_time = time.time()  # 记录串行爬取电影详情页地址的起始时间
    get(urls)
    print(detail_urls)
    end_time = time.time()  # 记录串行爬取电影详情页地址结束时间
    print('串行爬取电影详情页地址耗时：', end_time - start_time)  # 4.719,12.56 添加2次数据处理后时间为：112.716，128.957
    start_time_4 = time.time()  # 记录串行爬取电影详情页地址的起始时间
    s = Spider()  # 创建自定义爬虫类对象
    pool = Pool(processes=4)  # 创建4进程对象map()函数会将第二个参数的需要迭代的列表元素一个个的传入第一个参数我们的函数中
    pool.map(s.get2, urls)
    pool.close()  # 有会更好，没有也可以指定自动停止。
    pool.join()  # 有会更好，没有也可以指定自动停止。
    print('s.detail_urls2', s.detail_urls2)  # 打印为空，子进程会完全复制一份主进程的资源, 创建一个独立的内存空间
    end_time_4 = time.time()  # 记录串行爬取电影详情页地址结束时间
    print('4进程爬取电影详情页地址耗时：', end_time_4 - start_time_4)  # 4.218,4.295 添加加次爬取后的时间为：23.580，21.724
