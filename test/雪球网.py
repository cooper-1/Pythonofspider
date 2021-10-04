# -*-coding:  UTF-8
# @Time    :  2021/9/29 14:49
# @Author  :  Cooper
# @FileName:  雪球网.py
# @Software:  PyCharm
"""
对雪球网中的新闻数据进行获取
https://www.xueqiu.com
"""
import requests

from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Cookie': 'device_id=2ce0346bfb06227ec3e215367ead7820; Hm_lvt_1db88642e346389874251b5a1eded6e3=1632898314; remember=1; xq_a_token=dea63308e60bb64bb3ebb7175de4887071ad2299; xqat=dea63308e60bb64bb3ebb7175de4887071ad2299; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjc0OTA3OTc2OTEsImlzcyI6InVjIiwiZXhwIjoxNjM1NDkwNDg0LCJjdG0iOjE2MzI4OTg0ODQ1NjEsImNpZCI6ImQ5ZDBuNEFadXAifQ.dKPw89vt-gCZWBNxuUftDVTtow8Z0tOyFI33I5Poj_MgjO5T6gGVOwPUJZzFufarTEbMgerjCIImQgn8A2ZuCPLcz6KCrva7o1PB1UltmwVaWkqVKyqNXVUXN6maA_5ot5MHbLRFyZNh1Or13uQK7mnxrE2J0BwXxEKL89TFBhOjJ2bn0VE5hM-P72nh5TOSZDKA9X6dEeKtVvTy0Ftj024KK7_fv-7kjHB8QSB5TaEHiYNQ_6ytGtVEoo5be_EXGkUieHWm78hFY_DH2-WM_pDDUuvqYwIcwB4K90WBXKNaIzYYEt1Er1rtSw91bTA39sK6gBsYSJuxu80JNMkWGA; xq_r_token=966e35d252ea2cdaeefbec951abe2a34b94b38fe; xq_is_login=1; u=7490797691; s=cf1f38ofph; bid=73bd92ebe18eef8d6fa6e800064c1efd_ku570im5; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1632901012'
}
url = 'https://im1.xueqiu.com/im-comet/v2/notifications/381388/ping.json?user_id=7490797691'
page_text = requests.get(url=url, headers=headers)
print(page_text.content.decode('utf-8'))  # 带上Cookie  可以拿到
