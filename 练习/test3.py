# -*-coding:  UTF-8
# @Time    :  2021/11/4 19:42
# @Author  :  Cooper
# @FileName:  test3.py
# @Software:  PyCharm

import requests
import random
import csv
import time
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import json
import jsonpath

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
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
ctime = time.strftime("%Y-%m-%d", time.localtime())


def getlist(url):
    # 获取列表URL
    try:
        start = time.time()
        header = {'User-Agent': random.choice(user_agent_list),
                  }  # 随机选一个user-agent
        data = {
            'AreaID': '',
            'RiverID': '',
            'MNName': '',
            'PageIndex': '1',
            'PageSize': '60',
            'action': 'getRealDatas'}
        res = requests.post(url, params=data, timeout=20)
        print('第一次·网络状态码: ', res.status_code)
        # print(res.content)
        end = time.time()
        print('爬取时间为：' + str(end - start))
        # print(res.content.decode('utf-8'))
        result = json.loads(res.content.decode('utf-8'))
        result2 = jsonpath.jsonpath(result, '$.thead')
        print(result2[0])
        print('-' * 50)
        result3 = jsonpath.jsonpath(result, '$.tbody')
        print(result3[0][2])
        with open("数据%s.csv" % ctime, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(result2[0])
            w.writerows(result3[0])
        return res.content

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # url = 'http://106.37.208.243:8068/GJZ/Ajax/Publish.ashx'
    # url = 'http://106.37.208.243:8068/GJZ/Ajax/Publish.ashx'
    url = 'http://106.37.208.243:8068/GJZ/Business/Publish/Main.html?nsukey=izcwxfBd9wvE6xZJmS9DC%2BOo7fv7ybS8nnsrmgK4cyMrp54jCB0NEXQBVjHOqwFgPrUPw2B8TL6b2mQbPLe4HWhy0yPx80Vj1mmfXMC4nBUa3naLxIrNOvCXjHO4a25yILUSi%2Fu7K%2F2QrmjBVN1DaQ9k1056DUZQRdPPYtpWzEWXHPpeZoHNvcoDS0EtEC6HodxX7A34wVTWuAOGl5kh9w%3D%3D'
    url = 'http://106.37.208.243:8068/GJZ/Business/Publish/Main.html?nsukey=izcwxfBd9wvE6xZJmS9DC%2BOo7fv7ybS8nnsrmgK4cyMrp54jCB0NEXQBVjHOqwFgPrUPw2B8TL6b2mQbPLe4HWhy0yPx80Vj1mmfXMC4nBUa3naLxIrNOvCXjHO4a25yILUSi%2Fu7K%2F2QrmjBVN1DaQ9k1056DUZQRdPPYtpWzEWXHPpeZoHNvcoDS0EtEC6HodxX7A34wVTWuAOGl5kh9w%3D%3D'
    url = 'http://106.37.208.243:8068/GJZ/Ajax/Publish.ashx'
    getlist(url)
