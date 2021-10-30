# -*-coding:  UTF-8
# @Time    :  2021/10/28 11:56
# @Author  :  Cooper
# @FileName:  测试format.py
# @Software:  PyCharm
# juzicode.com/vx:桔子code
a = 3
b = 5.12345
c = '桔子code'
d = [1, 2, 3, 4, 5]
e = (1, 2, 3, 4, 5)
f = {1, 2, 3, 4, 5}

out = 'a:{0},b:{1},c:{2},d:{3},e:{4},f:{5}'.format(a, b, c, d, e, f)
print('字符串转换后', out)