# -*-coding:  UTF-8
# @Time    :  2021/10/6 22:54
# @Author  :  Cooper
# @FileName:  sub方法.py
# @Software:  PyCharm
import re

pattern = r'1[345798]\d{9}'
string = '中奖号码为： 645645541 联系电话为: 18819776051'
result = re.sub(pattern, '1xxxxxxxxxx', string)
print(result)
