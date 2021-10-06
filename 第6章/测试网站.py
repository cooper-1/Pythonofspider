# -*-coding:  UTF-8
# @Time    :  2021/10/6 13:08
# @Author  :  Cooper
# @FileName:  测试网站.py
# @Software:  PyCharm
import requests
import requests_cache

# 使用requests_cache()方法
requests_cache.install_cache()

# 清除已有的缓存
requests_cache.clear()

# 访问自己用flask创建的简易系统
url = 'http://127.0.0.1:5000/'

# 创建session会话
session = requests.session()
# 执行两次访问：
for t in range(2):
    req = session.get(url)
    # from_cache是requests_cache的函数，如果输出True，说明生成缓存
    print(req.from_cache)

