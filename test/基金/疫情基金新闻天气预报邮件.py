# -*-coding:  UTF-8
# @Time    :  2021/6/6 12:09
# @Author  :  Cooper
# @FileName:  天气预报疫情美图新闻邮件.py
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

i = 0
j = 1

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
    msgtext = MIMEText(
        '<!DOCTYPE html> <html> <head> <meta charset="utf-8" /> <title>闰京的消息</title> </head> <body><font size=10>'
        + ctime + '</font><font size=6> <br />' + news + result + '</font><' + '<br><img src="cid:image1"><br>'
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
        print('第%s轮·getlist1·获取图片集列表·第一次网络状态码:' % i, res.status_code)
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
    print('第%s轮·getlist2·下载图片· 第二网络状态码:' % i, res.status_code)
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
        epidemic = ''.join(getlist4('https://ncov.dxy.cn/ncovh5/view/pneumonia'))
        sendmail('<ul class="t clearfix">' + result[0] + '</ul>' + ''.join(epidemic))

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


def getlist4(url):
    # 爬取疫情新闻数据
    try:
        global i
        i = i + 1
        ctime = strftime("%Y-%m-%d", localtime())
        # print(ctime)
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=10)
        print('第%s轮，getlist4·网络状态码:' % i, res.status_code)
        # print(res.content)

        pattern2 = re.compile(',"pubDateStr":"(.*?),"infoSource":"央视新闻app","sourceUrl":', re.S)  # 综合得分
        result2 = pattern2.findall(res.content.decode('utf-8'))
        # print(''.join(result2))
        a = (str('\n'.join(result2))).replace('\\n', '')  # 替换\n
        # print(a)
        # print((''.join(result2)))
        # filename = os.getcwd()
        path = os.getcwd() + '\\疫情新闻'
        if not os.path.exists(path):
            print(path)
            os.makedirs(path)
            print('目录创建成功')
        # print(path)
        with open(path + '/%s.txt' % ctime, 'a+', encoding='utf-8') as fp:
            fp.write(ctime + '\n')
            fp.write(a + '\n')
            print('疫情新闻写入成功')

        return a

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
