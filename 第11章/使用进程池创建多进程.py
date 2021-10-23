# -*-coding:  UTF-8
# @Time    :  2021/10/18 22:10
# @Author  :  Cooper
# @FileName:  使用进程池创建多进程.py
# @Software:  PyCharm
from multiprocessing import Pool
import os, time


def task(name):
    print('子进程（%s）执行task %s...' % (os.getpid(), name))
    time.sleep(1)


if __name__ == '__main__':
    print('______________________父进程开始执行————————————————————————')
    print('父进程PID： %s' % os.getpid())  # 输出当前程序的PID
    p = Pool(3)
    for i in range(10):
        p.apply_async(task, args=(i,))  # 使用非阻塞方式
    print('等待所有子进程结束‘’‘’')
    p.close()  # 关闭进程池，关闭后p不再接受新的请求
    p.join()  # 等待子进程结束
    print('所有子进程结束')
