# -*-coding:  UTF-8
# @Time    :  2021/10/6 13:07
# @Author  :  Cooper
# @FileName:  网站.py
# @Software:  PyCharm
from flask import Flask

# 创建一个Flask实例
app = Flask(__name__)


# 设置路由，即url
@app.route('/')
# url对应的函数
def hello_rc():
    # 返回的页面
    return "Hello Requests-cache"


# 程序运行
if __name__ == '__main__':
    app.run()
