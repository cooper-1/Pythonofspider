# -*-coding:  UTF-8
# @Time    :  2021/10/30 11:12
# @Author  :  Cooper
# @FileName:  NaN数据处理.py
# @Software:  PyCharm
import pandas as pd
import numpy

data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 26, 36, 46, 56], }

data_frame = pd.DataFrame(data)

print(data_frame)
data_frame['A'][0] = numpy.nan
print(data_frame)
print('每列空缺值数量为：\n', data_frame.isnull().sum())
print('每列非空缺值数量为：\n', data_frame.notnull().sum())
data_frame.dropna(axis=0, inplace=True)
print(data_frame)
