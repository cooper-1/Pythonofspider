# -*-coding:  UTF-8
# @Time    :  2021/10/3 12:08
# @Author  :  Cooper
# @FileName:  爬取基金.py
# @Software:  PyCharm
# 导入需要的模块
import requests
import time
import csv
import re


class TtFundSpider:
    """天天基金爬取"""

    def __init__(self, page):
        self.API_URL = 'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36 FS'
        }
        self.TIMESTRF = int(time.time()) * 1000
        self.page = page

    def get_params(self):
        """
        构建params参数的方法
        :return:
        """
        params = {
            "t": "1",
            "lx": "1",
            "letter": "",
            "gsid": "",
            "text": "",
            "sort": "zdf,desc",
            "page": f"{str(self.page)},200",
            "dt": str(self.TIMESTRF),
            "atfc": "",
            "onlySale": "0",
        }
        return params

    def parse_url(self, url):
        """
        发送请求，获取响应数据的方法
        :param url:
        :return:
        """
        params = self.get_params()
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.content.decode()

    def get_data(self, data_str):
        """
        提取基金数据的方法
        :param data_str:
        :return:
        """
        str_data = re.findall('var db=.*,datas:(.*),count:.*}', data_str, re.S)[0]
        data_list = eval(str_data)
        for data in data_list:
            yield {
                '基金代码': data[0],
                '基金简称': data[1],
                '单位净值': data[3],
                '累计净值': data[4],
                '日增长值': data[6],
                '日增长率': data[7],
                '手续费': data[17]
            }

    def run(self):
        """
        实现主要逻辑思路
        :return:
        """
        with open('./jjData.csv', 'a', encoding='utf-8-sig', newline="") as csvfile:
            fieldnames = ['基金代码', '基金简称', '单位净值', '累计净值', '日增长值', '日增长率', '手续费']
            write_dict = csv.DictWriter(csvfile, fieldnames=fieldnames)
            write_dict.writeheader()
            # 发送请求，获取响应数据
            data_str = self.parse_url(self.API_URL)
            # 提取数据
            fund_data_list = self.get_data(data_str)
            for fund_data in fund_data_list:
                print(fund_data)
                # 保存数据
                write_dict.writerow(fund_data)


if __name__ == '__main__':
    for page in range(1, 6):
        ttFund_spider = TtFundSpider(page)
        ttFund_spider.run()
