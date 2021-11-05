# -*-coding:  UTF-8
# @Time    :  2021/10/31 19:33
# @Author  :  Cooper
# @FileName:  创建数据库文件.py
# @Software:  PyCharm
import sqlite3

# 数据库文件是Mrsofo.db ，如果文件不存在就自动创建
conn = sqlite3.connect('Mrsofo.db')
# 创建一个cursor
cursor = conn.cursor()
# 执行一条SQL语句，创建user表
cursor.execute('create table user (id int(10) primary key , name varchar (20))')
# 关闭游标
cursor.close()
# 关闭Connection
conn.close()
