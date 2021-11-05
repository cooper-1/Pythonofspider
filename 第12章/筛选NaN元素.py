# -*-coding:  UTF-8
# @Time    :  2021/10/30 12:02
# @Author  :  Cooper
# @FileName:  筛选NaN元素.py
# @Software:  PyCharm
import pandas as pd
import numpy

data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 26, 36, 46, 56]}
data_frame = pd.DataFrame(data)

print(data_frame)
data_frame['A'][0] = numpy.nan
data_frame['A'][1] = numpy.nan
data_frame['A'][2] = numpy.nan
data_frame['A'][3] = numpy.nan
data_frame['A'][4] = numpy.nan
data_frame.dropna(how='all', axis=1, inplace=True)
print(data_frame)
