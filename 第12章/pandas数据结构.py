# -*-coding:  UTF-8
# @Time    :  2021/10/30 10:15
# @Author  :  Cooper
# @FileName:  pandas数据结构.py
# @Software:  PyCharm
import pandas as pd

data = ['A', 'B', 'C', ]
index = ['a', 'b', 'c']
series = pd.Series(data, index=index)
print(series)
print('索引数组为：', series.index)
print('元素数组为：', series.values)
print('指定下标的数组元素为：', series[1])
print('指定元素的数组元素为：', series['a'])
print('获取多个下标对应的series对象：\n', series[1:3])
print('获取多个索引对应的series对象：\n', series[['a', 'b']])
series[0] = 'D'
print('修改下标为0的元素值：\n', series)
series['b'] = 'F'
print('修改下标为0的元素值：\n', series)
