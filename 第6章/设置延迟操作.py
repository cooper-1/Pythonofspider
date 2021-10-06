# -*-coding:  UTF-8
# @Time    :  2021/10/6 11:50
# @Author  :  Cooper
# @FileName:  设置延迟操作.py
# @Software:  PyCharm
import requests_cache
# import requests
import time

version = requests_cache.__version__
print('模块版本为： ', version)
requests_cache.install_cache()  # 设置缓存
requests_cache.clear()  # 清理缓存

# url = 'http://httpbin.org/get'
url = 'http://127.0.0.1:5000/'

# response = requests.get(url)
# print('是否存在缓存： ', response.from_cache)
i = 0


def make_throttle_hook(timeout=0.1):
    def hook(response, *args, **kwargs):
        global i
        i = i + 1
        print('eeee')
        print(response.text)
        # 判断没有缓存时就添加延时
        if not getattr(response, 'from_cache', False):
            print('没有缓存')
            print('等待', timeout, '秒!')
            time.sleep(timeout)
        else:
            print('是否存在请求缓存！', response.from_cache)  # 存在缓存输出True
        return response

    return hook


if __name__ == '__main__':
    requests_cache.install_cache()  # 设置缓存
    requests_cache.clear()  # 清理缓存
    s = requests_cache.CachedSession()  # 创建缓存会话
    s.hooks = {'response': make_throttle_hook(3)}  # 配置钩子函数
    print(i)
    s.get(url)
    print(i)
    s.get(url)
    print(i)
    s.get(url)
    print(i)
