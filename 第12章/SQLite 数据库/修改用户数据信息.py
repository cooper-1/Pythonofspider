# -*-coding:  UTF-8
# @Time    :  2021/10/31 21:19
# @Author  :  Cooper
# @FileName:  修改用户数据信息.py
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
# cursor.execute('select * from user ')
# # 执行查询语句
# result3 = cursor.fetchone()  # 查询一条数据
# print(result3)
cursor.execute('update user set name = ? where id = ?', ('MR', 1))
cursor.execute('select * from user ')
result3 = cursor.fetchall()  # 查询一条数据
print(result3)
# 删除用户数据
cursor.execute('delete from user where id = ? ',(1,))
cursor.execute('select * from user ')
result3 = cursor.fetchall()  # 查询一条数据
print(result3)
