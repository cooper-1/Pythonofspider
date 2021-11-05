# -*-coding:  UTF-8
# @Time    :  2021/10/31 21:57
# @Author  :  Cooper
# @FileName:  连接数据库.py
# @Software:  PyCharm
import pymysql

db = pymysql.connect('localhost', 'root', '1274814498', 'test', charset='utf8')
# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()
# 使用 execute（）方法执行SQL查询
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print('Database version :%s' % data)
sql = """
CREATE TABLE urls(
id int NOT NULL AUTO_INCREMENT,
name varchar (50) NOT NULL ,
category varchar (50) NOT NULL ,
price decimal (10,2) DEFAULT NULL ,
publish_time date DEFAULT NULL ,
PRIMARY KEY (id) 
) ENGINE = MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
cursor.execute('DROP TABLE IF EXISTS `urls`')
cursor.execute(sql)
data = [
    ('零基础学Python', 'python', '79.80', '2018-5-20'),
    ('python 从入门到精通', 'python', '69.80', '2018-6-18'),
    ('零基础学PHP', 'PHP', '79.80', '2016-5-21'),
    ('零基础学Java', 'Java', '59.80', '3017-5-11'),
]
try:
    # 执行SQL语句，插入多条数据
    cursor.executemany("insert into urls(name,category,price,publish_time) values (%s ,%s, %s ,%s )", data)
    # 提交数据
    db.commit()
except:
    # 发生错误时回滚
    db.commit()

db.close()
