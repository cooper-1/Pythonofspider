# -*-coding:  UTF-8
# @Time    :  2021/9/29 16:25
# @Author  :  Cooper
# @FileName:  url的编码与解码.py
# @Software:  PyCharm
import urllib.parse

base_url = 'https://developers.weixin.qq.com/get?'
params = {'name': 'jack', 'country': '中国', 'age': 30}
url = base_url + urllib.parse.urlencode(params)
print(url)
print(base_url + urllib.parse.quote('泽成'))
print(urllib.parse.unquote(url))
q = urllib.parse.urlsplit(url).query
q_dict = urllib.parse.parse_qs(q)
q_dict2 = urllib.parse.parse_qsl(q)
print(q_dict)  # 字典
print(q_dict2)  # 元组组成的列表
