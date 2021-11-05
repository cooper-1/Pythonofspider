# -*-coding:  UTF-8
# @Time    :  2021/11/3 13:13
# @Author  :  Cooper
# @FileName:  正则、、.py
# @Software:  PyCharm
import re

notip = []

ip = []
with open('test.txt', 'r', encoding='utf-8') as fp:
    content = fp.read()
    # print(content)
    # pattern = re.compile(r'[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', re.S)
    pattern = re.compile(r'(?!([0-9]{0,3}\.){3}[0-9]{0,3}).+', re.S)
    result = pattern.findall(content)
    print(result)
with open('test.txt', 'r', encoding='utf-8') as fp:
    content = fp.readlines()
    for i in content:
        i = i.strip()
        notip.append(i)
        # print(i)
        pattern = re.compile(r'[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
        result = pattern.findall(i)
        if result:
            ip.append(result[0])
    # print(ip)
print(set(notip) - set(ip))
