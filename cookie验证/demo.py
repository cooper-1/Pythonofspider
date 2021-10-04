import requests  # 导入网络请求模块
from lxml import etree  # 导入lxml模块

cookies = 'll="118285"; bid=ZKJd6eVb_l8; __guid=236236167.3307123070475795000.1611500943290.067; __utmv=30149280.23134; __yadk_uid=xoRS2jDnitcjEsVL7BVKZmsEK9aDSOCZ; _vwo_uuid_v2=DA2A6B99F333EC041E5A01F04391A4947|11ce7325df322eac8e28eb33c94edeaf; __gads=ID=76b48cd70afc6a66-22d347a0e7c5003f:T=1612192560:RT=1612192560:S=ALNI_Mbqg0LFyJ6Psz1mlvdA2Uyqoz9pGw; gr_user_id=1d01b238-76ad-4f7e-9d48-c7a4e7c9072a; ap_v=0,6.0; __utma=30149280.186945708.1611500946.1628931325.1632904948.11; __utmc=30149280; __utmz=30149280.1632904948.11.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1632905009%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmain%22%5D; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; dbcl2="231344732:C11wkua2Yhc"; ck=CZPD; monitor_count=7; _pk_id.100001.8cb4=384475d84ab15d36.1611500944.7.1632905403.1628931321.; __utmb=30149280.23.9.1632905403562'
headers = {'Host': 'www.douban.com',
           'Referer': 'https://www.hao123.com/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/72.0.3626.121 Safari/537.36'}
# 创建RequestsCookieJar对象，用于设置cookies信息
cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=', 1)
    cookies_jar.set(key, value)  # 将cookies保存RequestsCookieJar当中
# 发送网络请求
response = requests.get('https://www.douban.com/',
headers=headers, cookies=cookies_jar)
if response.status_code == 200:  # 请求成功时
    html = etree.HTML(response.text)  # 解析html代码
    # 获取用户名
    name = html.xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]/text()')
    print(name[0])  # 打印用户名




