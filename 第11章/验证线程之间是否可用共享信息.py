# -*-coding:  UTF-8
# @Time    :  2021/10/17 12:24
# @Author  :  Cooper
# @FileName:  验证线程之间是否可用共享信息.py
# @Software:  PyCharm
from threading import Thread
import time

g_num = 100


def plus():
    print('——————————————————————子线程1开始————————————————————')
    global g_num
    for i in range(3):
        time.sleep(1)
        g_num += 50
        print('g_num plus 50 equals to  %s' % g_num)
    print('——————————————————————子线程1结束————————————————————')


def minus():
    print('——————————————————————子线程2开始————————————————————')
    global g_num
    for i in range(3):
        time.sleep(1)
        g_num -= 50
        print('g_num minus 50 equals to %s' % g_num)
    print('——————————————————————子线程2结束————————————————————')


if __name__ == '__main__':
    print('主线程开始')
    # 创建4个线程，存入列表
    print('g_num is %s' % g_num)
    t1 = Thread(target=plus)
    t2 = Thread(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程结束')
