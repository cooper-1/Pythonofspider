# -*-coding:  UTF-8
# @Time    :  2021/10/17 17:54
# @Author  :  Cooper
# @FileName:  使用队列在进程间通信.py
# @Software:  PyCharm
from queue import Queue
import random, threading, time


# 生产者类
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print('%s将产品%d加入队列' % (self.getName(), i))
            self.data.put(i)
            time.sleep(random.random())  # random() 方法返回随机生成的一个实数，它在[0,1)范围内。
        print('%s生产完成！' % self.getName())


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print('%s将产品%d从队列中取出' % (self.getName(), val))
            self.data.put(i)
            time.sleep(random.random())
        print('%s消费完成！' % self.getName())


if __name__ == '__main__':
    print('主线程开始')
    queue = Queue()  # 实例化队列
    producer = Producer('生产者', queue)  # 实例化线程Producer，并传入名字和队列作为参数
    consumer = Consumer('消费者', queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('主线程结束')
