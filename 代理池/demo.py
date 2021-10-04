import requests  # 导入网络请求模块

# 头部信息
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.121 Safari/537.36'}
proxy = {'http': 'http://116.140.53.173:22016',
         'https': 'https://116.140.53.173:22016'}  # 设置代理ip与对应的端口号http': 'http://165.225.208.100:10605'}, {'http': 'http://165.225.240.110:10605'}]
try:
    # 对需要爬取的网页发送请求
    # response = requests.get('https://httpbin.org/get', headers=headers, timeout=3)
    # response = requests.get('https://httpbin.org/get', headers=headers, proxies=proxy,verify=False, timeout=5)
    response = requests.get('http://202020.ip138.com', headers= headers,proxies=proxy,timeout=3)
    print(response.status_code)  # 打印响应状态码
    print(response.content)  # 打印响应状态码
except Exception as e:
    print('错误异常信息为：', e)  # 打印异常信息
