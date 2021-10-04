# -*-coding:  UTF-8
# @Time    :  2021/9/29 15:42
# @Author  :  Cooper
# @FileName:  爬取雪球网.py
# @Software:  PyCharm
import requests
import json

url = {
    'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=-1&count=10&category=111',
    'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=184275&count=15&category=111',
    'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=184086&count=15&category=111'
}

headers = {
    "Accept": "*/*",
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "aliyungf_tc=AQAAANr3VBkMZAgAUhVFeTTWn+RvdBpU; xq_a_token=584d0cf8d5a5a9809761f2244d8d272bac729ed4; xq_a_token.sig=x0gT9jm6qnwd-ddLu66T3A8KiVA; xq_r_token=98f278457fc4e1e5eb0846e36a7296e642b8138a; xq_r_token.sig=2Uxv_DgYTcCjz7qx4j570JpNHIs; _ga=GA1.2.1187356785.1534314931; _gid=GA1.2.1120971600.1534314931; Hm_lvt_1db88642e346389874251b5a1eded6e3=1534314931; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1534314931; u=331534314932251; device_id=7bdbd08983b2b7e03fd0747d6a121e99",
    "Host": "xueqiu.com",
    "Referer": "https://xueqiu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}
# 遍历3个链接
for url_url in url:
    response = requests.get(url_url, headers=headers)
    #转换为dict类型
    res_dict = json.loads(response.text)
    # print(type(res_dict))
    # 获取部分list信
    res_list = res_dict['list']
    # print(type(res_list))
    # 遍历获取的信息
    for res in res_list:
        data = res['data']
        # print(data)
        # 转换为dict类型
        data_dict = json.loads(data)
        # print(type(data_dict))
        # 转换为str类型
        data_id = str(data_dict['id'])
        data_title = str(data_dict['title'])
        data_description = str(data_dict['description'])
        data_target = str(data_dict['target'])
        data = ('用户id:' + data_id, '标题：' + data_title, '描述：' + data_description,'目标：' + data_target)

        print(data)