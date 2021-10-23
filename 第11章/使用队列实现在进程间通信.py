# -*-coding:  UTF-8
# @Time    :  2021/10/19 23:12
# @Author  :  Cooper
# @FileName:  使用队列实现在进程间通信.py
# @Software:  PyCharm
from multiprocessing import Process, Queue
import time


# 向队列中写入数据
def write_task(q):
    if not q.full():
        for i in range(5):
            message = '消息' + str(i)
            q.put(message)
            print('已经写入%s' % message)


# 从队列里面读取数据
def read_task(q):
    time.sleep(1)
    while not q.empty():
        print('已经读取： %s' % q.get(True, 2))


if __name__ == '__main__':
    print('主进程开始')
    q = Queue()
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('主进程结束')
