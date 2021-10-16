# -*-coding:  UTF-8
# @Time    :  2021/10/6 18:06
# @Author  :  Cooper
# @FileName:  requ2.py
# @Software:  PyCharm
import os
import time
from requests.exceptions import ReadTimeout, HTTPError, RequestException
from requests_html import HTMLSession
from fake_useragent import UserAgent

i = 0
location = os.getcwd() + '/fake_useragent_0.1.11.json'


def getlist(url):
    # 获取列表URL
    try:
        global i
        i += 1
        start = time.time()
        session = HTMLSession()  # 创建HTML会话对象
        header = {'useragent': UserAgent(path=location).random}
        res = session.get(url, headers=header, timeout=20)
        res.encoding = 'gb2312'
        print('第 %s 次·网络状态码: ' % i, res.status_code)
        if res.status_code == 200:
            # print(res.content)
            end = time.time()
            print('爬取时间为：' + str(end - start))
            return res
        else:
            raise Exception('不给访问')

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = 'https://blog.csdn.net/qq_51408776/article/details/114646430?utm_source=app&app_version=4.5.4'
    getlist(url)
