# -*-coding:  UTF-8
# @Time    :  2021/11/5 19:55
# @Author  :  Cooper
# @FileName:  滑动拼图验证码.py
# @Software:  PyCharm
from selenium import webdriver  # 导入webdriver
import re  # 导入正则模块
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()  # 谷歌浏览器
driver.get('http://sck.rjkflm.com:666/spider/jigsaw/')  # 启动网页
action = webdriver.ActionChains(driver)  # 创建动作
swiper = driver.find_element_by_xpath('//div[@class="handle"]/span[@class="swiper"]')  # 获取按钮滑块
# print(swiper)
action.click_and_hold(swiper).perform()  # 单击并保证不松开
# 滑动0距离,不松手，不执行该动作无法获取图形滑块left值
action.move_by_offset(0, 0).perform()
verify_style = driver.find_element_by_xpath('//div[@class="imgBox"]/div[@class="verify"]').get_attribute('style')
# 获取空缺滑块样式
verified_style = driver.find_element_by_xpath('//div[@class="imgBox"]/div[@class="verified"]').get_attribute('style')
# 获取空缺滑块left值
verified_left = float(re.findall('left: (.*?)px;', verified_style)[0])
print(verified_style)
print(verified_left)
# 获取图形滑块left值
verify_left = float(re.findall('left: (.*?)px;', verify_style)[0])
print(verify_left)
print(verified_left - verify_left)
action.move_by_offset(verified_left - 10, 0)  # 滑动指定距离
action.release().perform()  # 松开鼠标
