# -*-coding:  UTF-8
# @Time    :  2021/10/5 23:25
# @Author  :  Cooper
# @FileName:  cache.py
# @Software:  PyCharm
import requests_cache
import requests

version = requests_cache.__version__
print('模块版本为： ', version)
requests_cache.install_cache()  # 设置缓存
requests_cache.clear()  # 清理缓存
url = 'http://httpbin.org/get'
response = requests.get(url)
print('是否存在缓存： ', response.from_cache)
# response = requests.get(url)
# print('是否存在缓存： ', response.from_cache)
