# -*-coding:  UTF-8
# @Time    :  2021/9/29 14:00
# @Author  :  Cooper
# @FileName:  拆分URL.py
# @Software:  PyCharm
import urllib.parse

url = 'https://blog.csdn.net/Jerry_wo/article/details/107981463?ops_request_misc=&request_id=&biz_id=102&utm_term=%E7%88%AC%E5%8F%96%E9%9B%AA%E7%90%83%E7%BD%91&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-107981463.pc_search_result_control_group&spm=1018.2226.3001.4187'
pase_result = urllib.parse.urlparse(url)
print(pase_result)
print(urllib.parse.urlsplit(url)[0])
