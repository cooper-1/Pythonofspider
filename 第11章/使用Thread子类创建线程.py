# -*-coding:  UTF-8
# @Time    :  2021/10/17 12:14
# @Author  :  Cooper
# @FileName:  使用Thread子类创建线程.py
# @Software:  PyCharm
import threading
import time


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = '子线程' + self.name + '执行， i= ' + str(i)
            print(msg)


if __name__ == '__main__':
    print('主线程开始')
    t1 = SubThread()  # 创建子线程
    t2 = SubThread()
    t1.start()  # 启动子线程
    t2.start()
    time.sleep(5)
    print('我在等待中')
    t1.join()  # 等待 子线程
    t2.join()
    print('主线程结束')
