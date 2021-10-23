# -*-coding:  UTF-8
# @Time    :  2021/10/20 22:51
# @Author  :  Cooper
# @FileName:  爬取电影详情页地址.py
# @Software:  PyCharm
from agency.requ2 import getlist
import time
import re
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


class Spider():
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


if __name__ == '__main__':
    urls = ['https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'.format(str(i)) for i in range(1, 11)]
    start_time = time.time()  # 记录串行爬取电影详情页地址的起始时间
    get(urls)
    print(detail_urls)
    end_time = time.time()  # 记录串行爬取电影详情页地址结束时间
    print('串行爬取电影详情页地址耗时：', end_time - start_time)  # 4.719,12.56

    start_time_4 = time.time()  # 记录串行爬取电影详情页地址的起始时间
    s = Spider()  # 创建自定义爬虫类对象
    pool = Pool(processes=4)  # 创建4进程对象map()函数会将第二个参数的需要迭代的列表元素一个个的传入第一个参数我们的函数中
    pool.map(s.get2, urls)
    pool.close()  # 有会更好，没有也可以指定自动停止。
    pool.join()  # 有会更好，没有也可以指定自动停止。
    print('s.detail_urls2', s.detail_urls2)  # 打印为空，子进程会完全复制一份主进程的资源, 创建一个独立的内存空间
    end_time_4 = time.time()  # 记录串行爬取电影详情页地址结束时间
    print('4进程爬取电影详情页地址耗时：', end_time_4 - start_time_4)  # 4.218,4.295
