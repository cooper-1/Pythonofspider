# -*-coding:  UTF-8
# @Time    :  2021/9/30 20:53
# @Author  :  Cooper
# @FileName:  关卡一.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import re
import time
import random
from lxml import etree

j = 0
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


def getlist(url):
    # 获取列表URL
    try:
        global j
        j += 1
        count = 0
        header = {'User-Agent': random.choice(user_agent_list),
                  'Cookie': '__guid=55289773.11468598099655942000.1633006269675.4712; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1633006271; _ga=GA1.2.62432872.1633006271; _gid=GA1.2.286791808.1633006271; __gads=ID=73c714377ebe5b97-2287aec2fecb001f:T=1633006270:RT=1633006270:S=ALNI_MYezbMPw0YAn3k3jcymwbvd-K1xkA; footprints=eyJpdiI6ImhhQjFoWVd4RUk0dzJ3djdkMUNONlE9PSIsInZhbHVlIjoidDVJV3RkK1JNdVVNcGErOVwvRGxObDRRNzJBN0pHeUF6d2hVRkV4WElpdlhkUm8xRTVVcGpVZVRxenl2RmZRM20iLCJtYWMiOiI3N2U4OGM5NGZjNDlmZDgxY2Y1MWJhYWE3ZjhmYzkxNGIyNmZhZjZmMTczNjU4MDg4YzBkOTllZDAwMmQ5NmM1In0%3D; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IkdRZnl3TDZWVmJaYmczOXB3N2F5U2c9PSIsInZhbHVlIjoiOXBhZFJoVld2ekphcHRhSTNSZjFnV0xFYUJQWkVISWRxbXpvVGFudXgrT0hVODZjakFhcFd2NmZVNEQydkRMWkJ3NkpVUlR1ZndETTZ3TUJWWEJBUHptT2pSQ3ZnSGNrcG15VEVXeFJcL1NiVzlzclVsYlBLNHAxMit5b3k3RnBpSGNyZzVPcGp4eWQ4endXakJzUTNjK2dYRDRvdEdcL0l1Q3JhSmtzVFRTSG89IiwibWFjIjoiZjhjYWZkZmRkMDdmOGQ3YWI5ZWQ2YmZhYzdjM2ExOTgwOWM4ZjI1NTcwODgwZDhmZTI2MzdlOTU1NTNmZjU2YSJ9; XSRF-TOKEN=eyJpdiI6IjRCYllHMkx1SzhUNW9DdCtQYjhyNGc9PSIsInZhbHVlIjoiNURtOVVKeTl2MDdZTEp5Q3poSTRXZTRVMTJwM1gxNVE2ZkZ0OU5FazJORWlHQnAyUFlUSmxRbXpKRnQ1aFR1TSIsIm1hYyI6IjY5ZTAxN2MwMDhjMzIxYjU3M2M0ODQxMmJmYjE5MWE1MGU3YzMyM2Y2ZGVhNjlkOTYyNWI4MGYyZmI5MDc2YzYifQ%3D%3D; glidedsky_session=eyJpdiI6InArTWIyYmkzcXprb2NlQUswNFpJWGc9PSIsInZhbHVlIjoiU3dtU0RDNURnbUx0MmM5ME8zUzh4OFk1eE5ZSWZtM0p6cUFGSjhvR3dRSXlKZHF1NUFIRmdcL2U1a0pzUndFVG8iLCJtYWMiOiIzMmFlN2Y0MWRkYzAwZGM0NjM2YWZiYzRmMDUwYjZhYzNjMzcwMmE2ZTc0ZjAyYmRlY2VmMjMzY2NiZThkY2U4In0%3D; monitor_count=10; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1633006378'}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=20)
        print('第%s轮，第一次·网络状态码: ' % j, res.status_code)
        # print(res.content.decode('utf-8'))
        html = etree.HTML(res.content)
        result = html.xpath('//div[@class="col-md-1"]/text()')
        # print(result)
        for i in result:
            print(i.strip())
            count += int(i.strip())
        print(count)

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = 'http://www.glidedsky.com/level/web/crawler-basic-1'
    getlist(url)
