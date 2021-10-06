# -*-coding:  UTF-8
# @Time    :  2021/10/6 16:19
# @Author  :  Cooper
# @FileName:  强大的requests-HTML模块.py
# @Software:  PyCharm
from requests_html import HTMLSession

session = HTMLSession()  # 创建HTML会话对象
url = 'http://news.youth.cn/'  # 中国青年网
r = session.get(url)  # 发送网络请求
print(r.html)  # 打印网络请求的url地址
