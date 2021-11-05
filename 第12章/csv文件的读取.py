# -*-coding:  UTF-8
# @Time    :  2021/10/30 12:37
# @Author  :  Cooper
# @FileName:  csv文件的读取.py
# @Software:  PyCharm
import pandas as pd

data = pd.read_csv('test.csv')
print(data)
data.to_csv('new_test.csv', columns=['B', 'C'], index=False)
new_data = pd.read_csv('new_test.csv')
print('读取的新的CSV文件的内容为：\n',new_data)
