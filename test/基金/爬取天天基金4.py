# -*-coding:  UTF-8
# @Time    :  2021/10/4 10:23
# @Author  :  Cooper
# @FileName:  爬取天天基金4.py
# @Software:  PyCharm
from agency import requ
from lxml import etree
import re

url = 'http://fund.eastmoney.com/012414.html?spm=search'  # 招商中证白酒指数(LOF)C
url = 'http://fund.eastmoney.com/161725.html?spm=search'  # 招商中证白酒指数(LOF)A
response = requ.getlist(url).decode('utf-8')
# print(response.decode('utf-8'))

# 基金涨跌
pattern = re.compile('<div class="poptableWrap singleStyleHeight01">(.*?)<div class="poptableWrap_', re.S)
port = pattern.findall(response)
print(port[0])

print('_' * 50)  # 基金持股
pattern = re.compile('<div class=\'poptableWrap\'>(.*?)<span class=\'end_date\'>', re.S)
port = pattern.findall(response)
print(''.join(port))

print('~' * 50)  # 基金信息
pattern = re.compile('<div class="fundDetail-main">(.*?)<div class="choseBuyWay canBuy">', re.S)
port = pattern.findall(response)
print(''.join(port))

response = etree.HTML(response)
a = response.xpath("//div[@style='float: left']/text()")
print(a[0])  # 基金名字
b = response.xpath('//div[@class="estimatedchart hasLoading"]//img/@src')
print(b[0])  # 净值估算图
imgsrc = 'http:' + b[0]
print(imgsrc)
file_name = a[0]
with open(file_name + '.jpg', 'wb') as f:
    f.write(requ.getlist(imgsrc))
