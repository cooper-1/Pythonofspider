# -*-coding:  UTF-8
# @Time    :  2021/10/4 18:09
# @Author  :  Cooper
# @FileName:  统计天数.py
# @Software:  PyCharm

import datetime
import time

today = datetime.date.today()
print(today)
# begindays = input("Please input your's begindays:")
begindays = '20110101'
# begindays = '2021-10-01'
# 输入格式为 20110101
chdays = time.strptime(begindays, "%Y%m%d")
# print("We together count days:", (today - datetime.date(2021 10 01).days, "Days!"))
print(chdays)
print(chdays[:3])
print(type(chdays[:3]))
# print(type(*chdays[:3]))
print(*chdays[:3])
print(type(5))
print(*chdays[:3])
print('-'*50)
print((today - datetime.date(*chdays[:3])).days)
print((today - datetime.date(*chdays[:3])))

print("We together count days:", (today - datetime.date(*chdays[:3])).days, "Days!")
a = (2021, 1, 1)
print(a)
print(*a)


# 可变参数解包
def f(*args):
    print(args)


l = [1, 2, 3, 4, 5, 6]
f(*l)
# 2021 1 1

# 可变关键词参数解包
def f(**kwargs):
    print(kwargs)


l = {'a': "python", 'b': "C++"}  # 必须是字典
f(**l)

