# -*-coding:  utf-8 -*-
# @Time    :  2021/1/28 23:16
# @Author  :  Cooper
# @FileName:  proxies.py
# @Software:  PyCharm

import requests
import re
import random

user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    ": Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19                                                      *                                   .0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

proxylist = [
    {"http": "http://175.43.130.154:9999"},
    {"http": "http://183.166.20.129:9999"},
    {"http": "http://106.110.195.3:9999"},
    {"http": "http://175.44.108.75:9999"},
    {"http": "http://49.86.26.166:9999"},
    {"http": "http://113.121.37.248:9999"}
]

proxieslist = []


class Proxy:
    def __init__(self):
        self.i = 100

    def getproxy(self):
        url = 'https://www.89ip.cn/tqdl.html?num={}&address=&kill_address=&port=&kill_port=&isp='.format(self.i)
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        proxy = random.choice(proxylist)  # 随机选一个ip地址
        res = requests.get(url, headers=header, proxies=proxy, timeout=10)
        print('第一次·网络状态码： ', res.status_code)
        # print(res.content.decode('utf-8'))
        pattern = re.compile('<br>(.*?)<br>', re.S)
        result = pattern.findall(res.text)
        url = 'http://www.baidu.com/'
        print(result)
        for proxy in result:
            proxy = {"http": "http://%s" % proxy}
            # print(proxy)
            try:
                header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
                res = requests.get(url, headers=header, proxies=proxy, timeout=2)
                flag = True
            except:
                flag = False

            if flag:
                proxieslist.append(proxy)
        print(len(proxieslist))
        print(proxieslist)
        if proxieslist:
            return proxieslist


if __name__ == "__main__":
    a = Proxy()
    b = a.getproxy()
    print(b)
