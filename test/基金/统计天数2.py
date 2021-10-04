# -*-coding:  UTF-8
# @Time    :  2021/10/4 20:22
# @Author  :  Cooper
# @FileName:  统计天数2.py
# @Software:  PyCharm
import datetime
import time
from time import localtime, strftime

today = datetime.date.today()
print(today)
print(type(today))
startTime = strftime("%Y-%m-%d", localtime())
print(startTime)
print(type(startTime))
ctime = '2021-10-01'
print(ctime)
print(type(ctime))
chdays = time.strptime(ctime, "%Y-%m-%d")  # 重新将日期<class 'str'>格式回<class 'time.struct_time'>类型
print(*chdays[:3])
print(type(chdays))
print(type(datetime.date(*chdays[:3])))  # datetime.date(*chdays[:3])).days变为<class 'datetime.date'>类型
print((today - datetime.date(*chdays[:3])).days)  # 这样才能统计时间
