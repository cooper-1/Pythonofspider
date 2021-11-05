# -*-coding:  UTF-8
# @Time    :  2021/10/30 12:31
# @Author  :  Cooper
# @FileName:  存取CSV文件.py
# @Software:  PyCharm
import pandas as pd

data = {'A': [1, None, 1, 1, 5], 'B': [6, 7, None, 9, 10], 'C': [11, 12, 13, None, 15], 'D': [16, 26, 36, 46, None]}
data_frame = pd.DataFrame(data)
print(data_frame)
data_frame.to_csv('test.csv')
