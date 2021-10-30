from os import path
import requests
from bs4 import BeautifulSoup
import json
import pymysql
import numpy as np

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0'  # 请求地址
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}  # 创建头部信息
response = requests.get(url, headers=headers)  # 发送网络请求
content = response.content.decode('utf-8')

soup = BeautifulSoup(content, 'html.parser')
listA = soup.find_all(name='script', attrs={"id": "getAreaStat"})
listB = soup.find_all(name='script', attrs={"id": "getListByCountryTypeService2"})
# listA = soup.find_all(name='div',attrs={"class":"c-touchable-feedback c-touchable-feedback-no-default"})
account = str(listA)

messages = account[52:-21]
messages_json = json.loads(messages)

valuesList = []
cityList = []

for i in range(len(messages_json)):
    # value = messages_json[i]
    ##全国各省
    value = (messages_json[i].get('provinceName'), messages_json[i].get('provinceShortName'),
             messages_json[i].get('currentConfirmedCount'), messages_json[i].get('confirmedCount'),
             messages_json[i].get('suspectedCount'), messages_json[i].get('curedCount'),
             messages_json[i].get('deadCount'), messages_json[i].get('comment'), messages_json[i].get('locationId'),
             messages_json[i].get('statisticsData'), messages_json[i].get('CreateTime'))
    valuesList.append(value)
    cityValue = messages_json[i].get('cities')
    # print(cityValue)

    for j in range(len(cityValue)):
        cityValueList = (
        cityValue[j].get('cityName'), cityValue[j].get('currentConfirmedCount'), cityValue[j].get('confirmedCount'),
        cityValue[j].get('suspectedCount'), cityValue[j].get('curedCount'), cityValue[j].get('deadCount'),
        cityValue[j].get('locationId'), messages_json[i].get('provinceShortName'))
        # print(cityValueList)
        cityList.append(cityValueList)
    # cityList.append(cityValue)
db = pymysql.connect("localhost", "root", "root", "payiqing", charset='utf8')
cursor = db.cursor()
array = np.asarray(valuesList[0])
sql_clean_city = "TRUNCATE TABLE city_map"
sql_clean_json = "TRUNCATE TABLE province_data_from_json"
sql_clean_province = "TRUNCATE TABLE province_map"
sql1 = "INSERT INTO city_map values (%s,%s,%s,%s,%s,%s,%s,%s)"
##全国各省
sql = "INSERT INTO province_map values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

value_tuple = tuple(valuesList)
cityTuple = tuple(cityList)
worldTuple = tuple(worldList)

try:
    cursor.execute(sql_clean_province)

    db.commit()
except:
    print('执行失败，进入回调1')
    db.rollback()

try:
    cursor.execute(sql_clean_city)

except:
    print('执行失败，进入回调2')
    db.rollback()
try:

    cursor.executemany(sql, value_tuple)

    db.commit()
except:
    print('执行失败，进入回调3')
    db.rollback()

try:

    cursor.executemany(sql1, cityTuple)
    db.commit()
except:
    print('执行失败，进入回调4')
    db.rollback()

db.close()