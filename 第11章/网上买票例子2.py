# -*-coding:  UTF-8
# @Time    :  2021/10/17 15:37
# @Author  :  Cooper
# @FileName:  网上买票例子2.py
# @Software:  PyCharm
# encoding:utf-8
import threading
import time

lock = threading.Lock()
k = 20


def dance():
    global k
    while k > 0:
        lock.acquire()
        if k > 0:
            time.sleep(0.2)
            k -= 1
            lock.release()
            print("{}卖出一张票还剩下{}".format(threading.current_thread().name, k))
        else:
            print("票卖完了")
            break


t1 = threading.Thread(target=dance, name="线程一")
t2 = threading.Thread(target=dance, name="线程二")
t1.start()
t2.start()
t1.join()
t2.join()
