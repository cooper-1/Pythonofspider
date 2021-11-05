# -*-coding:  UTF-8
# @Time    :  2021/11/4 19:25
# @Author  :  Cooper
# @FileName:  test2.py
# @Software:  PyCharm
from selenium import webdriver
import time, re

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
url = 'http://106.37.208.243:8068/GJZ/Business/Publish/Main.html'
driver.get(url)
time.sleep(15)
print(driver.page_source)
pattern = re.compile(r'<html lang="en" style="font-size(.*?)新客首月NaN元，立即开通VIP', re.S)
result = pattern.findall(driver.page_source)
result = re.findall(r'[\u4e00-\u9fa5]+', ''.join(result))
with open('baidu.txt', 'w') as f:
    for index, item in enumerate(result):
        if index % 11 == 0: f.write('\n')
        f.write('  ' + item)
driver.quit()
