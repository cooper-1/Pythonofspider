# -*-coding:  UTF-8
# @Time    :  2021/10/26 9:58
# @Author  :  Cooper
# @FileName:  疫情3.py
# @Software:  PyCharm
import random
import os
import re
import json
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime
import time
import datetime

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

newdata = []
data = [['中华人民共和国', '中国', 2528, 125620, 2030, 117396, 5696]]


def getlist4(url='https://ncov.dxy.cn/ncovh5/view/pneumonia'):
    # 爬取疫情新闻数据
    try:
        global i
        i += 1
        # 获取今天（现在时间）
        today = datetime.datetime.today()
        ctime = strftime("%Y-%m-%d", localtime())
        path = os.getcwd() + '\\疫情新闻'
        yesterday = (today - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        with open(path + "/疫情%s.csv" % yesterday, 'r', ) as f:
            r = f.readlines()[-1].split(',')[:-3]
            data.append(r)
        # print(ctime)
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        response = requests.get(url, headers=header, timeout=10)
        print('第%s轮，getlist4·网络状态码:' % i, response.status_code)
        print(response.content.decode('gb2312',errors=True))
        # with open('yiqing.html', 'w') as fp:
        with open('yiqing.html', 'w', encoding='utf-8') as fp:
            fp.write(response.content.decode('utf-8'))
            # fp.write(response.content)

        content = response.content.decode('utf-8')

        soup = BeautifulSoup(content, 'html.parser')
        listA = soup.find_all(name='script', attrs={"id": "getAreaStat"})
        print('-' * 80)
        print(listA)
        account = str(listA)
        messages = account[52:-21]  # 头去除了[<script id="getAreaStat">try { window.getAreaStat =
        # 尾巴去除了}catch(e){}</script>]
        print('-' * 80)
        print(messages)
        messages_json = json.loads(messages)  # 读取文件中的字符串元素，转化成Python类型
        print('_' * 80)
        print(messages_json)

        valuesList = []
        cityList = []

        for i in range(len(messages_json)):
            # value = messages_json[i]
            print(messages_json[i])
            ##全国各省
            value = (messages_json[i].get('provinceName'), messages_json[i].get('provinceShortName'),
                     messages_json[i].get('currentConfirmedCount'), messages_json[i].get('confirmedCount'),
                     messages_json[i].get('suspectedCount'), messages_json[i].get('curedCount'),
                     messages_json[i].get('deadCount'), messages_json[i].get('comment'),
                     messages_json[i].get('locationId'),
                     messages_json[i].get('statisticsData'), messages_json[i].get('CreateTime'))
            valuesList.append(value)
            cityValue = messages_json[i].get('cities')  # get():返回的是object对象
            print(cityValue)
            print('*' * 80)
            for j in range(len(cityValue)):
                cityValueList = (
                    cityValue[j].get('cityName'), cityValue[j].get('currentConfirmedCount'),
                    cityValue[j].get('confirmedCount'),
                    cityValue[j].get('suspectedCount'), cityValue[j].get('curedCount'), cityValue[j].get('deadCount'),
                    cityValue[j].get('locationId'), messages_json[i].get('provinceShortName'))
                print(cityValueList)
                cityList.append(cityValueList)

        value_tuple = tuple(valuesList)
        cityTuple = tuple(cityList)
        print(value_tuple)
        print(cityTuple)

        if not os.path.exists(path):
            print(path)
            os.makedirs(path)
            print('目录创建成功')
        print(value_tuple)
        present = 0
        sums = 0
        suspected = 0
        cure = 0
        dead = 0
        for var in value_tuple:
            # print(var[3])
            present += var[2]
            sums += var[3]
            suspected += var[4]
            cure += var[5]
            dead += var[6]
        print(present)
        print(sums)
        print(suspected)
        print(cure)
        print(dead)
        data.append(['中华人民共和国', '中国', present, sums, suspected, cure, dead])
        print(data[-2])
        print(data[-1])

        for i, datum in enumerate(data[-1][2:]):
            print('datum', i, datum)
            print(int(data[-2][2:][i]))
            print(datum, '-', int(data[-2][2:][i]), '=', datum - int(data[-2][2:][i]))
            print('_' * 80)
            newdata.append(datum - int(data[-2][2:][i]))  # 单个对象用append ，多个对象用extend
            print('-' * 80)
        print(newdata)  # [8, 66, 0, 58, 0]
        with open(path + "/疫情-1%s.csv" % ctime, 'w', encoding='UTF-8-sig', newline='') as f:
            w = csv.writer(f)
            a = ['省名', '简称', '现存确诊', '累计确诊', '怀疑确诊', '治愈', '死亡', '备注', 'locationId', 'statisticsData']
            w.writerow(a)
            w.writerows(value_tuple)  # 注意这里#写入多行
            w.writerow(['中华人民共和国', '中国', present, sums, suspected, cure, dead])  # 注意这里#写入多行
            w.writerow(['新增加数据', '新增', newdata[0], newdata[1], newdata[2], newdata[3], newdata[4]])  # 注意这里#写入多行
            # w.writerows(cityTuple)  # 注意这里#写入多行
            print('疫情数据写入成功')
            print(value_tuple)




    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    getlist4()
