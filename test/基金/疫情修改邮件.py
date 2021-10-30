# -*-coding:  UTF-8
# @Time    :  2021/10/27 15:03
# @Author  :  Cooper
# @FileName:  疫情修改邮件.py
# @Software:  PyCharm
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import re
import random
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import schedule
import time
import os
from time import localtime, strftime
from lxml import etree
import datetime
import json
from bs4 import BeautifulSoup
import csv
from time import localtime, strftime

i = 0
j = 1
newdata = []
data = [['中华人民共和国', '中国', 2528, 125620, 2030, 117396, 5696]]

startTime = strftime("%Y-%m-%d", localtime())

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


def sendmail(result):
    # 请自行修改下面的邮件发送者和接收者
    global j
    # print('newdata', newdata)
    sender = "yx1274814498@163.com"  # 发送方地址
    receivers = ['yx1274814498@163.com', '1274814498@qq.com', '1506262492@qq.com', '1651122140@qq.com',
                 '763184952@qq.com',
                 '770031105@qq.com', '1593809016@qq.com']  # "1274814498@qq.com,770031105@qq.com,yx1274814498@163.com"
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = "yx1274814498@163.com"
    message['To'] = 'yx1274814498@163.com,770031105@qq.com,1274814498@qq.com'
    message['Subject'] = Header('1274814498@qq.com示例代码实验邮件', 'utf-8')
    # smtper = SMTP('smtp.163.com',465)
    smtper = smtplib.SMTP_SSL()
    smtper = smtplib.SMTP_SSL('smtp.163.com', 465)
    message = MIMEMultipart('related')
    message['Subject'] = 'Cooper’s Jarvis'
    # 爬取人民日报
    news = getlist5()

    # 爬取基金信息
    jj, name = getlist6('http://fund.eastmoney.com/161725.html?spm=search')
    ctime = strftime("%Y-%m-%d", localtime())
    yiqing = '现存确诊新增{}<br />累计确诊新增{}<br />怀疑确诊新增{}<br />累计治愈新增{}<br />累计死亡新增{}<br />'.format(newdata[0], newdata[1],
                                                                                             newdata[2], newdata[3],
                                                                                             newdata[4])
    msgtext = MIMEText(
        '<!DOCTYPE html> <html> <head> <meta charset="utf-8" /> <title>闰京的消息</title> </head> <body><font size=10>'
        + ctime + '</font><font size=6> <br />' + news + result + yiqing + '</font>' + '<br><img src="cid:image1"><br>'
        + jj + '<br><img src="cid:image2"><br>' + '</body></html>', 'html', 'utf-8')

    # 粘贴图片
    message.attach(msgtext)
    path = os.getcwd() + '\\每日图片'
    filename = path + '/%s-%s.jpg' % (ctime, j)

    fp = open(filename, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)

    path = os.getcwd() + '\\基金信息\\' + name
    filename2 = path + '/%s.jpg' % ctime
    # filename2 = name + ctime + '.jpg'
    fp = open(filename2, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image2>')
    message.attach(msgImage)

    # 请自行修改下面的登录口令
    smtper.ehlo()
    # smtper.starttls()
    smtper.login(sender, "SBMMBSAHCMPDUOWC")  # 此处secretpass输入授权码

    # 发送邮件，测试时注释掉
    smtper.sendmail(sender, receivers, message.as_string())
    before = time.strptime(startTime, "%Y-%m-%d")
    today = datetime.date.today()
    print('开始时间是：' + startTime + " 现在时间是： " + ctime + ' 共计 %s 天。 ' % (
            (today - datetime.date(*before[:3])).days + 1) + '总共发送了%s封邮件' % j)
    print('邮件发送完成!')
    smtper.quit()
    j += 1


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
        result = pattern.findall(res.content.decode('utf-8'))
        # print(result)
        # print(random.choice(result))
        url2 = (random.choice(result))
        url2 = 'https:' + url2
        print('url = ', url2)
        getlist2(url2)

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
    ctime = strftime("%Y-%m-%d", localtime())
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    res = requests.get(url, headers=header, timeout=10)
    print('第%s轮，getlist2·下载图片· 第二网络状态码:' % i, res.status_code)
    pattern = re.compile('img data-src="(.*?)"', re.S)  # class="preview" href=
    result = pattern.findall(res.text)
    # print('result===', result)
    list2 = []
    for url2 in result:
        list2.append('https:' + url2)
    # print(list2)
    # print(random.choice(list2))
    url2 = random.choice(list2)
    path = os.getcwd() + '\\每日图片'
    if not os.path.exists(path):
        print(path)
        os.makedirs(path)
        print('目录创建成功')
    # print(path)
    with open(path + '/%s-%s.jpg' % (ctime, j), 'wb') as f:
        f.write(requests.get(url2, headers=header, timeout=10).content)
        print('第%s次保存图片完成·' % j, url2)


def getlist3(url):
    # 爬取天气预报
    try:
        global i
        i = i + 1
        ctime = strftime("%Y-%m-%d", localtime())
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=20)
        print('第%s轮，getlist3·网络状态码:' % i, res.status_code, url)
        # print(res.content.decode('utf-8'))

        pattern = re.compile('<ul class="t clearfix">(.*?)</ul>', re.S)  # <img class="" src=
        result = pattern.findall(res.content.decode('utf-8'))
        path = os.getcwd() + '\\天气预报'
        if not os.path.exists(path):
            print(path)
            os.makedirs(path)
            print('目录创建成功')
        with open(path + '/%s.txt' % ctime, 'a+', encoding='utf-8') as fp:
            fp.write(ctime)
            fp.write(result[0])
            print('天气预报写入成功')

        # 爬取疫情新闻
        getlist4()
        sendmail('<ul class="t clearfix">' + result[0] + '</ul>')

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)
        getlist1()
        getlist3(url='http://www.weather.com.cn/weather/101281201.shtml')

def getlist4(url='https://ncov.dxy.cn/ncovh5/view/pneumonia'):
    # 爬取疫情新闻数据
    try:
        global i
        i += 1
        newdata.clear()
        # 获取今天（现在时间）
        today = datetime.datetime.today()
        ctime = strftime("%Y-%m-%d", localtime())
        path = os.getcwd() + '\\疫情新闻'
        yesterday = (today - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        # print(path + "/疫情%s.csv" % yesterday)
        with open(path + "/疫情%s.csv" % yesterday, 'r', errors='ignore') as f:
            # with open(path + "/疫情%s.csv" % yesterday, 'r') as f:
            r = f.readlines()[-2].rstrip().split(',')
            data.append(r)
        # print(ctime)
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        response = requests.get(url, headers=header, timeout=10)
        print('第%s轮，getlist4·网络状态码:' % i, response.status_code)
        # print(response.content.decode('utf-8'))
        with open('yiqing.html', 'w', encoding='utf-8') as fp:
            fp.write(response.content.decode('utf-8'))

        content = response.content.decode('utf-8')

        soup = BeautifulSoup(content, 'html.parser')
        listA = soup.find_all(name='script', attrs={"id": "getAreaStat"})
        # print('-' * 80)
        # print(listA)
        account = str(listA)
        messages = account[52:-21]  # 头去除了[<script id="getAreaStat">try { window.getAreaStat =
        # 尾巴去除了}catch(e){}</script>]
        # print('-' * 80)
        # print(messages)
        messages_json = json.loads(messages)  # 读取文件中的字符串元素，转化成Python类型
        # print('_' * 80)
        # print(messages_json)

        valuesList = []
        cityList = []

        for i in range(len(messages_json)):
            # value = messages_json[i]
            # print(messages_json[i])
            ##全国各省
            value = (messages_json[i].get('provinceName'), messages_json[i].get('provinceShortName'),
                     messages_json[i].get('currentConfirmedCount'), messages_json[i].get('confirmedCount'),
                     messages_json[i].get('suspectedCount'), messages_json[i].get('curedCount'),
                     messages_json[i].get('deadCount'), messages_json[i].get('comment'),
                     messages_json[i].get('locationId'),
                     messages_json[i].get('statisticsData'), messages_json[i].get('CreateTime'))
            valuesList.append(value)
            cityValue = messages_json[i].get('cities')  # get():返回的是object对象
            # print(cityValue)
            # print('*' * 80)
            for j in range(len(cityValue)):
                cityValueList = (
                    cityValue[j].get('cityName'), cityValue[j].get('currentConfirmedCount'),
                    cityValue[j].get('confirmedCount'),
                    cityValue[j].get('suspectedCount'), cityValue[j].get('curedCount'), cityValue[j].get('deadCount'),
                    cityValue[j].get('locationId'), messages_json[i].get('provinceShortName'))
                # print(cityValueList)
                cityList.append(cityValueList)

        value_tuple = tuple(valuesList)
        cityTuple = tuple(cityList)
        # print(value_tuple)
        # print(cityTuple)

        if not os.path.exists(path):
            print(path)
            os.makedirs(path)
            print('目录创建成功')
        # print(value_tuple)
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
        # print(present)
        # print(sums)
        # print(suspected)
        # print(cure)
        # print(dead)
        data.append(['中华人民共和国', '中国', present, sums, suspected, cure, dead])
        print(data[-2])
        print(data[-1])

        for i, datum in enumerate(data[-1][2:]):
            # print('datum', i, datum)
            # print(int(data[-2][2:][i]))
            # print(datum, '-', int(data[-2][2:][i]), '=', datum - int(data[-2][2:][i]))
            # print('_' * 80)
            newdata.append(datum - int(data[-2][2:][i]))  # 单个对象用append ，多个对象用extend
            # print('-' * 80)
        print(newdata)  # [8, 66, 0, 58, 0]
        with open(path + "/疫情%s.csv" % ctime, 'w', newline='') as f:
            w = csv.writer(f)
            a = ['省名', '简称', '现存确诊', '累计确诊', '怀疑确诊', '累计治愈', '累计死亡', '备注', 'locationId', 'statisticsData']
            w.writerow(a)
            w.writerows(value_tuple)  # 注意这里#写入多行
            w.writerow([None, None, present, sums, suspected, cure, dead])  # 注意这里#写入多行
            w.writerow(['新增加数据', '新增', newdata[0], newdata[1], newdata[2], newdata[3], newdata[4]])  # 注意这里#写入多行
            # w.writerows(cityTuple)  # 注意这里#写入多行
            print('疫情数据写入成功')
            # print(value_tuple)


    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)

def getlist5():
    # 爬取人民日报
    ctime = strftime("%Y-%m/%d", localtime())
    # print(ctime)
    url = 'http://paper.people.com.cn/rmrb/html/{}/nbs.D110000renmrb_01.htm'.format(ctime)
    global i
    i += 1
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    res = requests.get(url, headers=header, timeout=20)
    print('第%s轮，getlist5·网络状态码:' % i, res.status_code)
    html = etree.HTML(res.content)
    result = html.xpath('//div/ul/li/a/text()')
    # print(result)
    ctime = strftime("%Y-%m-%d", localtime())
    path = os.getcwd() + '\\人民日报'
    if not os.path.exists(path):
        print(path)
        os.makedirs(path)
        print('目录创建成功')
    # print(path)
    with open(path + '/%s.txt' % ctime, 'a+', encoding='utf-8') as fp:
        fp.write(ctime + '\n')
        fp.write('\n'.join(result) + '\n')
        print('人民日报写入成功')

    return '<br />'.join(result)  # 换行


def getlist6(url):
    # 爬取基金信息
    try:
        global i
        i = i + 1
        ctime = strftime("%Y-%m-%d", localtime())
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=20)
        print('第%s轮，getlist6·网络状态码:' % i, res.status_code, url)
        res = res.content.decode('utf-8')
        # 基金涨跌
        pattern = re.compile('<div class="poptableWrap singleStyleHeight01">(.*?)<div class="poptableWrap_', re.S)
        change = pattern.findall(res)
        # print(change[0])

        # print('_' * 50)  # 基金持股
        pattern = re.compile('<div class=\'poptableWrap\'>(.*?)<span class=\'end_date\'>', re.S)
        port = pattern.findall(res)
        # print(''.join(port))

        # print('~' * 50)  # 基金信息
        pattern = re.compile('<div class="fundDetail-main">(.*?)<div class="choseBuyWay canBuy">', re.S)
        message = pattern.findall(res)
        # print(''.join(message))

        res = etree.HTML(res)
        a = res.xpath("//div[@style='float: left']/text()")
        print(a[0])  # 基金名字
        b = res.xpath('//div[@class="estimatedchart hasLoading"]//img/@src')
        # print(b[0])

        imgsrc = 'http:' + b[0]  # 净值估算图
        # print(imgsrc)

        path = os.getcwd() + '\\基金信息'
        if not os.path.exists(path):
            print(path)
            os.makedirs(path)
            print('目录创建成功')
        path = path + '\\' + a[0]
        if not os.path.exists(path):
            print(path)
            os.makedirs(path)
            print('目录创建成功')

        # print(path)
        with open(path + '/%s.jpg' % ctime, 'wb') as f:
            f.write(requests.get(imgsrc).content)
            print('基金图片保存成功')

        return ('<div style="float: left">' + a[0] + '</div>' + change[0] + ''.join(port) + ''.join(message), a[0])

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    schedule.every().day.at("07:31").do(getlist1)
    schedule.every().day.at("12:31").do(getlist1)
    schedule.every().day.at("15:01").do(getlist1)

    # schedule.every(5).seconds.do(getlist1)
    # url = 'http://forecast.weather.com.cn/town/weather1dn/101280206003.shtml#input'  # 仁化
    url = 'http://www.weather.com.cn/weather/101280206.shtml'  # 仁化
    # url = 'http://www.weather.com.cn/weather/101280201.shtml'韶关

    schedule.every().day.at("07:33").do(getlist3, url)
    schedule.every().day.at("12:33").do(getlist3, url)
    schedule.every().day.at("15:03").do(getlist3, url)

    # 测试时使用，正式使用则注释掉
    # getlist1()
    # getlist3(url)

    while True:
        schedule.run_pending()
        time.sleep(1)
