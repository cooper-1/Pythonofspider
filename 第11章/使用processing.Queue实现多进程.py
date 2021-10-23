# -*-coding:  UTF-8
# @Time    :  2021/10/18 22:34
# @Author  :  Cooper
# @FileName:  使用processing.Queue实现多进程.py
# @Software:  PyCharm
from multiprocessing import Queue

if __name__ == '__main__':
    q = Queue(3)
    q.put('消息1')
    q.put('消息2')
    print(q.full())
    q.put('消息3')
    print(q.full())
    # 因为消息队列已经满，下面的try会抛出异常
    # 第一个try等待2秒报错，第二个立马报错
    try:
        q.put('消息4', True, 2)
    except:
        print('消息队列已经满了，现有的消息数量是：%s' % q.qsize())
    try:
        q.put_nowait('消息4')
    except:
        print('消息队列已经满了，现有的消息数量是：%s' % q.qsize())

    # 读取消息时候，先判断队列是否为空，为空时再读取
    if not q.empty():
        print('___________从队列中获取消息———————————————')
        for i in range(q.qsize()):
            print(q.get_nowait())
    if not q.full():
        q.put_nowait('消息4')
