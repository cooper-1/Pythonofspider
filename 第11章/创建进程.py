# -*-coding:  UTF-8
# @Time    :  2021/10/17 19:47
# @Author  :  Cooper
# @FileName:  创建进程.py
# @Software:  PyCharm
from multiprocessing import Process


def test(intercal):
    print('我是子进程')


def main():
    print('主进程开始')
    p = Process(target=test, args=(1,))
    p.start()
    print('主进程结束')


if __name__ == '__main__':
    main()
