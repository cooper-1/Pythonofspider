# -*-coding:  UTF-8
# @Time    :  2021/10/31 19:52
# @Author  :  Cooper
# @FileName:  操作SQLite.py
# @Software:  PyCharm
import sqlite3

# 数据库文件是Mrsofo.db ，如果文件不存在就自动创建
conn = sqlite3.connect('Mrsofo.db')
# 创建一个cursor
cursor = conn.cursor()
# 新增用户数据信息
cursor.execute('insert into user (id,name) values ("1","mrsofot")')
cursor.execute('insert into user (id,name) values ("2","Andy")')
cursor.execute('insert into user (id,name) values ("3","江闰京")')
# 执行查询语句
cursor.execute('select * from user where id > ?', (1,))
# cursor.execute('select * from user ')
# 获取查询结果
# result1 = cursor.fetchone()  # 查询一条数据
# result2 = cursor.fetchmany(2)
# result3 = cursor.fetchall()
result3 = cursor.fetchall()
# print(result1)
# print(result2)
print(result3)
# 关闭游标
cursor.close()
# 关闭Connection
conn.close()
