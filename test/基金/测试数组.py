# -*-coding:  UTF-8
# @Time    :  2021/10/27 14:29
# @Author  :  Cooper
# @FileName:  测试数组.py
# @Software:  PyCharm
i = [[1, 2, 3], [4, 5, 6], [7, 8, '9'], [1, 2, 3]]
print(i)
for k, j in enumerate(i[-1][2:]):
    print(j)
    print(k)
    print(int(i[-2][2:][k]))
    print(int(i[-2][2]))
    i[-2][2:][k] = int(i[-2][2:][k])
i[-2][2] = int(i[-2][2])
print(i)
