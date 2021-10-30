# -*-coding:  UTF-8
# @Time    :  2021/10/27 13:50
# @Author  :  Cooper
# @FileName:  获取日期.py
# @Software:  PyCharm
import datetime

# 获取今天（现在时间）
today = datetime.datetime.today()
# 昨天
yesterday = (today - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

# 明天
tomorrow = today + datetime.timedelta(days=1)

# 获取当前日期
date = datetime.date.today()
# 获取一秒后的时间
s = today + datetime.timedelta(seconds=1)
# 获取一分钟后的时间
m = today + datetime.timedelta(minutes=1)
# 获取一小时后的时间
h = today + datetime.timedelta(hours=1)
# 获取一年后的时间
y = today + datetime.timedelta(days=365)

print('获取今天（现在时间）：{}\n'.format(today),
      '昨天：{}\n'.format(yesterday),
      '明天：{}\n'.format(tomorrow),
      '获取当前日期：{}\n'.format(date),
      '一秒后的时间：{}\n'.format(s),
      '一分钟后的时间：{}\n'.format(m),
      '一小时后的时间：{}\n'.format(h),
      '一年后的时间：{}'.format(y))