# -*-coding:  UTF-8
# @Time    :  2021/11/3 12:05
# @Author  :  Cooper
# @FileName:  使用SQL.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import re
from time import localtime, strftime
import random
import os
import pymysql

user_agent_list = [ \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", \
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
i = 0
j = 0
list2 = []


def getlist1(url='https://search.bilibili.com/article?keyword=p%E7%AB%99'):
    # 获取图片列表URL
    try:
        global i
        i = i + 1
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=20)
        print('第%s轮，getlist1·获取图片集列表·第一次网络状态码:' % i, res.status_code)
        # print(res.content.decode('utf-8'))
        pattern = re.compile('<li class="article-item"><a href="(.*?)" title=', re.S)  # <img class="" src=
        result = ['https:' + i for i in pattern.findall(res.content.decode('utf-8'))]
        print(result)
        for url2 in result:
            # print(url2)
            getlist2(url2)
        down()
    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


def getlist2(url):
    # 下载图片
    global i
    i = i + 1
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    res = requests.get(url, headers=header, timeout=10)
    print('第%s轮，getlist2·下载图片· 第二网络状态码:' % i, res.status_code)
    pattern = re.compile('img data-src="(.*?)"', re.S)  # class="preview" href=
    result = pattern.findall(res.text)
    # print('result===', result)
    # list2 = []
    for url2 in result:
        list2.append('https:' + url2)
    print(list2)
    print(len(list2))


# 写入数据到mysql数据库

def down():
    db = pymysql.connect('localhost', 'root', '1274814498', 'test', charset='utf8')
    # db = pymysql.connect('localhost', 'root', '1274814498', 'test')
    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()
    # 使用 execute（）方法执行SQL查询
    sql = """
    CREATE TABLE urls(
    id int NOT NULL AUTO_INCREMENT,
    name varchar (100) NOT NULL , 
    PRIMARY KEY (id) 
    ) ENGINE = MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
    """
    cursor.execute('DROP TABLE IF EXISTS `urls`')
    cursor.execute(sql)

    try:
        # 执行SQL语句，插入多条数据
        cursor.executemany("insert into urls(name) values (%s)", list2)
        # 提交数据
        db.commit()
        print('写入成功')
    except Exception as e:
        print(e)
        # 发生错误时回滚
        db.commit()

    db.close()


if __name__ == '__main__':
    getlist1()
