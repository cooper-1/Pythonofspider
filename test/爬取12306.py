import requests
import re

# 导入Python SSL处理模块   Python 2.7.9 之后版本引入了一个新特性
import ssl

# 表示忽略未经核实的SSL证书认证
ssl._create_default_https_context = ssl._create_unverified_context


# 本案例基于机械工业出版社《Python网络爬虫从入门到精通》相关案例改写

def get_station():
    # 12306的城市名和城市代码js文件和URL
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9143'
    r = requests.get(url)
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'  # \u4e00-\u9fa5是所有汉字的Unicode编码范围
    result = re.findall(pattern, r.text)  # 按正则表达式匹配
    station = dict(result)
    print(station)
    return station


# 生成查询的URL
def get_query_url(text):
    # 城市名代码查询字典
    # key:城市名 value：城市代码，如：{'北京北': 'VAP', '北京东': 'BOP', '北京': 'BJP'}
    try:
        date = '2021-10-7'
        from_station_name = '沈阳'
        to_station_name = '鞍山'
        from_station = text[from_station_name]  # 将城市名转换为城市代码
        to_station = text[to_station_name]
    except:
        date, from_station, to_station = '--', '--', '--'
    # API URL构造
    url = (
        'https://kyfw.12306.cn/otn/leftTicket/query?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, from_station, to_station)
    return url


# 获取车次信息
def query_train_info(url, text):
    # 这部分在开发者控制台要全盘照自己浏览器显示的请求标头抄，经过实践验证，少一个都会被系统判定为爬虫，无法返回数据
    headers = {
        'Host': 'kyfw.12306.cn',
        'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E6%B2%88%E9%98%B3,SYT&ts=%E9%9E%8D%E5%B1%B1,AST&date=2020-06-24&flag=N,Y,Y',
        'Pragma': 'no-cache',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'br, gzip, deflate',
        'Cookie': '__guid=51538223.-125332947996240020000.1633232845803.5906; BIGipServerpool_index=821035530.43286.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=284164618.24610.0000; RAIL_EXPIRATION=1633567165726; RAIL_DEVICEID=RUZX2SGgoB9dpruiOJJnYQmqZ-JwLJRr4d03bw3dwwSCfK_PcQnR4GluEr7-EqqzjjCkqteIg6hgND8w02mU_qlD_HRRUYqspvdoS-82-PDup6qxA5tM_ZMcoyE6KpM3AjsRkSvcv-lq-HA9stW9v5BwGSvxVciE; monitor_count=2',
        'If-Modified-Since': '0',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
    }
    try:
        print('OK')
        r = requests.get(url, headers=headers)
        print(r.content.decode('utf-8'))
        print(r.json())
        # 获取返回json数据中data字段的result结果
        raw_trains = r.json()['data']['result']
        for raw_train in raw_trains:
            # 循环遍历每辆列车的信息
            data_list = raw_train.split('|')

            # 车次号码
            train_no = data_list[3]
            # 出发站
            from_station_code = data_list[6]
            from_station_name = text['沈阳']
            # 终点站
            to_station_code = data_list[7]
            to_station_name = text['鞍山']
            # 出发时间
            start_time = data_list[8]
            # 到达时间
            arrive_time = data_list[9]
            # 总耗时
            time_fucked_up = data_list[10]
            # 一等座
            first_class_seat = data_list[31] or '--'
            # 二等座
            second_class_seat = data_list[30] or '--'
            # 软卧
            soft_sleep = data_list[23] or '--'
            # 硬卧
            hard_sleep = data_list[28] or '--'
            # 硬座
            hard_seat = data_list[29] or '--'
            # 无座
            no_seat = data_list[26] or '--'
            # 打印查询结果
            info = (
                '车次:{}\n出发站:{}\n目的地:{}\n出发时间:{}\n到达时间:{}\n消耗时间:{}\n'
                '座位情况:\n一等座:「{}」\n二等座:「{}」\n软卧:「{}」\n硬卧:「{}」\n硬座:「{}」\n'
                '无座:「{}」\n\n'.format(train_no, from_station_name, to_station_name, start_time, arrive_time,
                                     time_fucked_up, first_class_seat,
                                     second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat)
            )
            print(info)
            print('ok2')
            if (second_class_seat and second_class_seat != '无' and train_no == 'G8070'):
                print('G8070次高铁二等座有票了\n', info)
                break;
            else:
                continue
    except Exception as e:
        print(e)


if __name__ == '__main__':
    text = get_station()
    url = get_query_url(text)
    # 循环查询，知道查询到想要的车次有票终止
    '''while True:
        time.sleep(1)#刷票频率
        if query_train_info(url,text):
            break'''
    query_train_info(url, text)
