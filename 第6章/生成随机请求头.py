# -*-coding:  UTF-8
# @Time    :  2021/10/6 16:38
# @Author  :  Cooper
# @FileName:  生成随机请求头.py
# @Software:  PyCharm
from requests_html import HTMLSession, UserAgent
# import random
import os

from fake_useragent import UserAgent

location = os.getcwd() + '/fake_useragent_0.1.11.json'
headers = {'useragent': UserAgent(path=location).random}

session = HTMLSession()  # 创建HTML会话对象
# data = {'user': 'admin', 'password': 123456}
# url = 'http://httpbin.org/post'
url = 'http://httpbin.org/get'
# print(ua)
# ua = UserAgent(use_cache_server=False)
# ua = UserAgent().random
# print(ua)
# # r = session.post(url, data, headers={'user-agent': ua})
r = session.get(url, headers=headers)
if r.status_code == 200:
    print(r.text)
# (Macintosh; Intel Mac OS X 10_12_6)
# .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0
ua = UserAgent(path=location)
#  'D:/BaiduNetdiskDownload/hello/venv/fake_useragent_0.1.11.json'   文件路径
# ie浏览器的user agent
print(ua.ie)
