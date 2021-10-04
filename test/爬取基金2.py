# -*-coding:  UTF-8
# @Time    :  2021/10/3 12:15
# @Author  :  Cooper
# @FileName:  爬取基金2.py
# @Software:  PyCharm

import requests
import execjs
import numpy as np
from matplotlib import pyplot as plt

url = "http://fund.eastmoney.com/pingzhongdata/519671.js?v=20201026224444"
content = requests.get(url)

jsContent = execjs.compile(content.text)
name = jsContent.eval('fS_name')
code = jsContent.eval('fS_code')

# 单位净值走势数据
netWorthTrendData = jsContent.eval('Data_netWorthTrend')
# 累计净值走势数据
ACWorthTrendData = jsContent.eval('Data_ACWorthTrend')

netWorthTrend = [v["y"] for v in netWorthTrendData]
ACWorthTrend = [v[1] for v in ACWorthTrendData]

plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 单位净值趋势图
plt.subplot(2, 1, 1)
plt.title(name + " ( " + code + " ) " + "单位净值")
plt.plot(netWorthTrend)

# 累计净值趋势图
plt.subplot(2, 1, 2)
plt.title(name + " ( " + code + " ) " + "累计净值")
plt.plot(ACWorthTrend)

plt.show()