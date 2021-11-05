# -*-coding:  UTF-8
# @Time    :  2021/10/30 12:10
# @Author  :  Cooper
# @FileName:  nan元素的替换.py
# @Software:  PyCharm
import pandas as pd
import numpy

data = {'A': [1, None, 3, 4, 5], 'B': [6, 7, None, 9, 10], 'C': [11, 12, 13, None, 15], 'D': [16, 26, 36, 46, None]}
data_frame = pd.DataFrame(data)
print(data_frame)
# data_frame.fillna(0, inplace=True)
# print(data_frame)
data_frame.fillna({'A': 0, 'B': 1, 'C': 2}, inplace=True)
print(data_frame)
