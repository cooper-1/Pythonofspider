# coding: utf-8
# http://wms.zjemc.org.cn/wms/wmsflex/index.html
import datetime
import pandas as pd
import urllib
import urllib.request as urllib2
from urllib.request import Request
import requests
import uuid
import pyamf
import json, datetime
from pyamf import remoting
from pyamf.flex import messaging
import re
import time
import csv


# 构造请求数据
def getRequestData():
    msg.body = []
    msg.headers['DSEndpoint'] = None
    msg.headers['DSId'] = str(uuid.uuid1()).upper()
    # 按AMF协议编码数据
    req = remoting.Request('null', body=(msg,))
    env = remoting.Envelope(amfVersion=pyamf.AMF3)
    env.bodies = [('/1', req)]
    data = bytes(remoting.encode(env).read())
    return data


# 返回一个请求的数据格式

def getResponse(data):
    url = 'http://wms.zjemc.org.cn/wms/messagebroker/amf'
    req = Request(url, data, headers={'Content-Type': 'application/x-amf'})
    # 解析返回数据
    opener = urllib2.build_opener()
    return opener.open(req).read()


def getContent(response):
    amf_parse_info = remoting.decode(response)
    info = amf_parse_info.bodies[0][1].body.body
    res = []
    for record in info:
        red = [record['mtName'], \
               record['monitorTime'], \
               record['boundaryArea'], \
               record['factorValues'], \
               record['factorLevel'], \
               ]
        res.append(red)
    return res


def printWaterList(ilt):
    tplt = "{0:20}\t{1:20}\t{2:20}\t{3:20}\t{4:20}"
    print(tplt.format("监测点", "监测时间", "监测点所属地区", "PH值、DO浓度（mg/l）、CODmn浓度（mg/l）、TP浓度（mg/l）、NH3-N浓度（mg/l）",
                      "PH值（级别）、DO浓度（级别）、CODmn浓度（级别）、TP浓度（级别）、NH3-N浓度（级别）"))
    output_list = ["监测点", "监测时间", "监测点所属地区", "PH值、DO浓度（mg/l）、CODmn浓度（mg/l）、TP浓度（mg/l）、NH3-N浓度（mg/l）",
                   "PH值（级别）、DO浓度（级别）、CODmn浓度（级别）、TP浓度（级别）、NH3-N浓度（级别）"]
    # 存储路径需根据需要更改
    data_str = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    print('data_str',data_str)
    with open("E:/python/浙江省地表水水质自动监测/%s_国家地表水水质自动监测系统检测数据.csv" % (data_str), "w+", encoding='GB18030',
              newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(output_list)
        csvfile.close()
    time.sleep(3)
    for g in ilt:
        out_putlist = [g[0], g[1], g[2], g[3], g[4]]
        print(out_putlist)
        time.sleep(1)  # 可省略，每打印一条，停一秒，再打印下一个
        # 存储路径需根据需要更改
        with open("E:/python/浙江省地表水水质自动监测/%s_国家地表水水质自动监测系统检测数据.csv" % (data_str), "a+", encoding='GB18030',
                  newline='') as csvfile:
            w = csv.writer(csvfile)
            w.writerow(out_putlist)
            csvfile.close()


class WmsHourDataVo:
    def __init__(self):
        None


pyamf.register_class(WmsHourDataVo, alias='com.fpi.prj.zjemc.airenv.wms.entity.vo')
msg = messaging.RemotingMessage(messageId=str(uuid.uuid1()).upper(),
                                clientId=str(uuid.uuid1()).upper(),
                                operation='getAllShowHourData',  # getAllValleyVo\getAllSiteHistoryVo
                                destination='GISCommonDataUtilForWms',
                                timeToLive=0,
                                timestamp=0, )

reqData = getRequestData()
rep = getResponse(reqData)
info = getContent(rep)
# 一次请求完成
reqData = getRequestData()
rep = getResponse(reqData)
res = getContent(rep)
printWaterList(res)
