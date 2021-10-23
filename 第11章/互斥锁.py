# -*-coding:  UTF-8
# @Time    :  2021/10/17 14:55
# @Author  :  Cooper
# @FileName:  互斥锁.py
# @Software:  PyCharm
from threading import Thread, Lock
import threading
import time

n = 100
mutex = Lock()


def task():
    global n
    while n > 0:
        mutex.acquire()  # 上锁
        if n > 0:
            n -= 1
            time.sleep(0.1)
            print('购买成功，剩余%d 张电影票' % n, '当前的线程是：', threading.current_thread().name)
        else:
            print('票已经卖完了')
            break
        mutex.release()


if __name__ == '__main__':
    print('主线程开始')
    t_l = []
    for i in range(10):
        t = Thread(target=task)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()
    print('主线程结束')
