# -*-coding:  UTF-8
# @Time    :  2021/10/30 12:18
# @Author  :  Cooper
# @FileName:  去除重复数据.py
# @Software:  PyCharm
import pandas as pd
import numpy

data = {'A': [1, None, 1, 1, 5], 'B': [6, 7, None, 9, 10], 'C': [11, 12, 13, None, 15], 'D': [16, 26, 36, 46, None]}
data_frame = pd.DataFrame(data)
print(data_frame)
data_frame.drop_duplicates('A', inplace=True)
newdata = data_frame.drop_duplicates()
print(data_frame)
print()
print(newdata)
data = {'A': [1, None, 1, 1, 5], 'B': [6, 6, None, 9, 10], 'C': [11, 11, 13, None, 15], 'D': [16, 26, 36, 46, None]}
data_frame = pd.DataFrame(data)
data_frame.drop_duplicates(subset=['C', 'B'], inplace=True)
print(data_frame)
