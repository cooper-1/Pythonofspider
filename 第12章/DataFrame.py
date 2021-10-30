# -*-coding:  UTF-8
# @Time    :  2021/10/30 10:31
# @Author  :  Cooper
# @FileName:  DataFrame.py
# @Software:  PyCharm
import pandas as pd

data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 26, 36, 46, 56], }

index = ['a', 'b', 'c', 'd', 'e']
data_frame = pd.DataFrame(data, index=index, columns=['B', 'C'])
data_frame['F'] = [17, 27, 37, 47, 57]
print(data_frame)
data_frame.drop(['a'], inplace=True)
print(data_frame)
print('-' * 80)
print(range(0, 2))
data_frame.drop(labels='B', axis=1, inplace=True)
print(data_frame)
data_frame = pd.DataFrame(data)
data_frame.drop(labels=range(0, 2), axis=0, inplace=True)
print(data_frame)
data_frame['A'][2] = 10
print(data_frame)
data_frame['B'] = [100, 110, 120]
print(data_frame)
print('指定列名的数据为：\n', data_frame['A'])
print('指定列名属性的数据为：\n', data_frame.D)
print('指定行索引范围的数据为：\n', data_frame[1:3])
print('指定列中的某个的数据为：\n', data_frame['B'][3])
