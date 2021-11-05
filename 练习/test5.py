# -*-coding:  UTF-8
# @Time    :  2021/11/4 20:45
# @Author  :  Cooper
# @FileName:  test5.py
# @Software:  PyCharm
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options     #建议使用谷歌浏览器
import time
chrome_options = Options()
chrome_options.add_argument('--headless')
#使不使用headless版本，也许你想感受一下浏览器自动打开，自动点击的快感，也不一定
browser = webdriver.Chrome(chrome_options=chrome_options)
#chromedriver下载下来之后复制到chrome.exe同文件夹下即可
print("打开网页中。。。")
browser.get("http://106.37.208.243:8068/GJZ/Business/Publish/Main.html")
print(browser.page_source)
print("网页响应中。。。")
wait = WebDriverWait(browser,20)#毕竟代码运行的速度和浏览器打开的速度不再一个量级，一个闪电侠，一个奥特曼
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,"mainframe")))#这一步很关键
browser.find_element_by_id('ddm_River').click()#模拟点击“流域”
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/ul/li[1]").click()#模拟点击“所有流域”
wait.until(EC.presence_of_element_located((By.CLASS_NAME,"grid")))#定位到数据
print("获取网页数据中。。。")
time.sleep(10)
soup = BeautifulSoup(browser.page_source,"lxml")
browser.close()
data_head = soup.select(".panel-heading")[0]
grid_data = soup.select(".grid")[0]
data_colhead = data_head.findAll("td")
data_rows = grid_data.findAll("tr")
water_df = pd.DataFrame(columns=[c.text for c in data_colhead])
print("提取网页数据中。。。")
for i,data_row in enumerate(data_rows):
	water_loc = water_df.iloc[:,0].values
	water_data = water_df.iloc[:,1].values
	row_dat = [r.text for r in data_row]
	water_df.loc[i] = row_dat
#系统时间
data_str = datetime.datetime.now().strftime('%Y_%m_%d')
#可修改保存路径
water_df.to_csv("E:/python/国家地表水爬虫/%s_国家地表水水质自动监测系统检测数据.csv" % (data_str),index=None, encoding="GB18030")
print("数据提取完成！！")