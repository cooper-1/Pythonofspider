# -*-coding:  UTF-8
# @Time    :  2021/10/18 22:22
# @Author  :  Cooper
# @FileName:  验证进程间能否共享信息.py
# @Software:  PyCharm
from multiprocessing import Process
import time

g_num = 100


def plus():
    print('——————————————————————子进程1开始————————————————————')
    global g_num
    for i in range(3):
        time.sleep(1)
        g_num += 50
        print('g_num plus 50 equals to  %s' % g_num)
    print('——————————————————————子进程1结束————————————————————')


def minus():
    print('——————————————————————子进程2开始————————————————————')
    global g_num
    for i in range(3):
        time.sleep(1)
        g_num -= 50
        print('g_num minus 50 equals to %s' % g_num)
    print('——————————————————————子进程2结束————————————————————')


if __name__ == '__main__':
    print('主进程开始')
    # 创建4个进程，存入列表
    print('g_num is %s' % g_num)
    t1 = Process(target=plus)
    t2 = Process(target=minus)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主进程结束')
