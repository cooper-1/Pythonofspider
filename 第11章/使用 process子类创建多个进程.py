# -*-coding:  UTF-8
# @Time    :  2021/10/17 21:03
# @Author  :  Cooper
# @FileName:  使用 process子类创建多个进程.py
# @Software:  PyCharm
from multiprocessing import Process
import time
import os


# 继承Process类
class SubProcess(Process):
    # 由于Process类本身也有__init__初始化方法，这个子类相当于重写了父类的这个方法
    def __init__(self, interval, name=''):
        Process.__init__(self)
        self.interval = interval
        if name:
            self.name = name

    def run(self):
        print('子进程（%s）开始执行，父进程为（%s）' % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)  # 程序将会被挂起interval秒
        t_end = time.time()
        print("子进程(%s)执行时间为'%0.2f'" % (os.getpid(), t_end - t_start))


if __name__ == '__main__':
    print('______________________父进程开始执行————————————————————————')
    print('父进程PID： %s' % os.getpid())  # 输出当前程序的PID
    p1 = SubProcess(interval=1, name='mrsoft')
    p2 = SubProcess(interval=2)
    # 对一个不包含target属性的Process类执行start（）方法，就会运行这个类的run（）方法
    # 所以这里会执行p1.run()
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
