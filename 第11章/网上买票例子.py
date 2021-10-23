# -*-coding:  UTF-8
# @Time    :  2021/10/17 15:28
# @Author  :  Cooper
# @FileName:  网上买票例子.py
# @Software:  PyCharm
import threading

list_ticket = []
lock = threading.Lock()  # 获取线程锁
num = 100
j = 0

for i in range(1, num + 1):
    ticket_num = '0' * (3 - len(str(i))) + str(i)
    list_ticket.append(ticket_num)


def seel_ticket(k):
    global list_ticket
    global j
    while 1:
        lock.acquire()
        print(k, '号正在打印票')
        if j != 100:
            thre = list_ticket[j]
            j += 1
            print(k, "号出票成功，票号为:", thre)
        else:
            print('票已经卖完')
            break
        lock.release()


list_thread = []
for i in range(10):
    thread = threading.Thread(target=seel_ticket, args=(i + 1,))
    list_thread.append(thread)
for i in list_thread:
    i.start()
