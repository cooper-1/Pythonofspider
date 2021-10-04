# -*-coding:  UTF-8
# @Time    :  2021/9/29 16:20
# @Author  :  Cooper
# @FileName:  连接URL.py
# @Software:  PyCharm
import urllib.parse

base_url = 'https://developers.weixin.qq.com'
print(urllib.parse.urljoin(base_url, 'miniprogram/dev/reference/configuration/page.html'))
print(urllib.parse.urljoin(base_url, 'https://developers.weixin.qq.com/miniprogram/dev/reference/configuration/page.html'))
