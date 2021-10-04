import urllib.request as urlreq
#输入代理IP及接口

proxyHost='117.94.176.254:10241'
#输入浏览网页地址
url='https://202020.ip138.com'
#设置代理
ph = urlreq.ProxyHandler({'https': 'https://'+proxyHost,'http': 'http://'+proxyHost})
oper = urlreq.build_opener(ph)
#设置头信息
headers = ('User-Agent','Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)')
oper.addheaders = [headers]
#headers = ('aaa','aaa')
#oper.addheaders = [headers]
#headers = ('bbb','bbb')
#oper.addheaders = [headers]
#提交请求
res = oper.open(url)
print(res.read())

