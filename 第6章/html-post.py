# -*-coding:  UTF-8
# @Time    :  2021/10/6 16:25
# @Author  :  Cooper
# @FileName:  html-post.py
# @Software:  PyCharm
from requests_html import HTMLSession

session = HTMLSession()  # 创建HTML会话对象
data = {'user': 'admin', 'password': 123456}
url = 'http://httpbin.org/post'
r = session.post(url, data)
if r.status_code == 200:
    print(r.text)
