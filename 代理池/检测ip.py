# -*-coding:  UTF-8
# @Time    :  2021/9/29 17:30
# @Author  :  Cooper
# @FileName:  检测ip.py
# @Software:  PyCharm
import requests

ip = "187.73.68.14:53281"
proxies = {"http": "http://" + ip}
try:
    requests.get('http://wenshu.court.gov.cn/', proxies=proxies)
except:
    print('失败')
else:
    print('成功')
