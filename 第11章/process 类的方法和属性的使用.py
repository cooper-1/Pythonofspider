# -*-coding:  UTF-8
# @Time    :  2021/10/17 20:01
# @Author  :  Cooper
# @FileName:  process 类的方法和属性的使用.py
# @Software:  PyCharm
from multiprocessing import Process
import time
import os


# 两个子进程将会调用的两个方法
def child(interval):
    print('子进程（%s）开始执行，父进程为（%s）' % (os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)  # 程序将会被挂起interval秒
    t_end = time.time()
    print("子进程(%s)执行时间为'%0.2f'" % (os.getpid(), t_end - t_start))


def child2(interval):
    print('子进程（%s）开始执行，父进程为（%s）' % (os.getpgid(), os.getppid()))
    t_start = time.time()
    time.sleep(interval)  # 程序将会被挂起interval秒
    t_end = time.time()
    print("子进程(%s)执行时间为'%0.2f'" % (os.getpid(), t_end - t_start))


if __name__ == '__main__':
    print('______________________父进程开始执行————————————————————————')
    print('父进程PID： %s' % os.getpid())  # 输出当前程序的PID
    p1 = Process(target=child, args=(1,))
    p2 = Process(target=child, name='mrsoft', args=(2,))
    p1.start()
    p2.start()
    # 同时父进程仍然往下执行，如果p2进程还在执行，将会返回True
    print('p1 is_alive = %s' % p1.is_alive())
    print('p2 is_alive = %s' % p2.is_alive())
    # 输出p1和p2 进程的别名和PID
    print('p1.name = %s' % p1.name)
    print('p1.pid = %s' % p1.pid)
    print('p1.name = %s' % p2.name)
    print('p1.pid = %s' % p2.pid)
    print('__________等待子进程————————————————————————')
    p1.join()
    p2.join()
    print('父进程结束')
'''进程相关函数：
os.getpid()
功能：获取一个进程的PID值
返回值：返回当前进程的PID
os.getppid()
功能：获取父进程的PID值
返回值：返回父进程PID
os._exit(status)
功能：结束一个进程
参数：进程的终止状态（随便输一个整数，eg：0，代表结束状态）
sys.exit([status])
功能：退出进程
参数：
整数：表示退出状态
字符串：表示退出时，打印内容
'''
