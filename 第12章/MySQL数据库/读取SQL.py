# -*-coding:  UTF-8
# @Time    :  2021/11/3 12:36
# @Author  :  Cooper
# @FileName:  读取SQL.py
# @Software:  PyCharm
import pymysql

db = pymysql.connect('localhost', 'root', '1274814498', 'test', charset='utf8')
# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
cursor.execute('select * from urls')
# result1 = [cursor.fetchall()]
result2 = list(cursor.fetchall())
# print(result1)
print(result2)
for i in result2:
    print(i[1])
