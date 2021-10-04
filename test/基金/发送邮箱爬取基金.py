# -*-coding:  UTF-8
# @Time    :  2021/10/4 12:29
# @Author  :  Cooper
# @FileName:  发送邮箱爬取基金.py
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

i = 0
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


def getlist(url):
    # 爬取天气预报
    try:
        global i
        i = i + 1
        ctime = strftime("%Y-%m-%d", localtime())
        header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
        res = requests.get(url, headers=header, timeout=20)
        print('第%s轮，getlist·网络状态码: ' % i, res.status_code, url)
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
        print(b[0])  # 净值估算图
        imgsrc = 'http:' + b[0]
        print(imgsrc)
        file_name = a[0] + ctime
        with open(file_name + '.jpg', 'wb') as f:
            f.write(requests.get(imgsrc).content)

        sendmail('<div style="float: left">' + a[0] + '</div>' + change[0] + ''.join(port) + ''.join(message), a[0])

    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')
    except ReadTimeout:
        print('time out')
    except Exception as e:
        print(e)


def sendmail(result, name):
    # 请自行修改下面的邮件发送者和接收者
    print(result)
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
    message['Subject'] = 'Cooper‘s Jarvis'

    msgText = MIMEText(
        '<!DOCTYPE html> <html> <head> <meta charset="utf-8" /> <title>闰京的消息</title> </head> <body><font size=6> ' + result
        + '</font><' + '<br><img src="cid:image1"><br></body></html>', 'html', 'utf-8')

    message.attach(msgText)
    ctime = strftime("%Y-%m-%d", localtime())
    filename = name + ctime + '.jpg'

    fp = open(filename, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)

    # 请自行修改下面的登录口令
    smtper.ehlo()
    # smtper.starttls()
    smtper.login(sender, "SBMMBSAHCMPDUOWC")  # 此处secretpass输入授权码
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')
    smtper.quit()


def getlist2(url):
    # 下载图片
    global i
    i = i + 1
    ctime = strftime("%Y-%m-%d", localtime())
    header = {'User-Agent': random.choice(user_agent_list)}  # 随机选一个user-agent
    res = requests.get(url, headers=header, timeout=10)
    print('第%s轮·getlist2·下载图片· 第二网络状态码：' % i, res.status_code)
    pattern = re.compile('img data-src="(.*?)"', re.S)  # class="preview" href=
    result = pattern.findall(res.text)
    # print('result===', result)
    list2 = []
    for url2 in result:
        list2.append('https:' + url2)
    # print(list2)
    print(random.choice(list2))
    url2 = random.choice(list2)
    filename = '%s.jpg' % ctime
    print('第%s次准备保存图片·' % i, url2)
    with open(filename, 'wb') as f:
        f.write(requests.get(url2, headers=header, timeout=10).content)


if __name__ == "__main__":
    url = 'http://fund.eastmoney.com/161725.html?spm=search'  # 招商中证白酒指数(LOF)A
    schedule.every().day.at("07:33").do(getlist, url)
    getlist(url)
    while True:
        schedule.run_pending()
        time.sleep(1)
