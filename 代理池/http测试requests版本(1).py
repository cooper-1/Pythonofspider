import requests


# 如果提示requests出错，可能需要安装request CMD运行 pip install requests
def get_proxy(headers):
    proxy_url = 'http://http.9vps.com/getip.asp?username=18819776051&pwd=bae276bac6e33746883cccdc3dd6519d&geshi=1&fenge=1&fengefu=&getnum=1'
    # proxy_url = 'http://http.9vps.com/getip.asp?username=test&pwd=test&geshi=1&fenge=1&fengefu=&getnum=1'
    aaa = requests.get(proxy_url, headers=headers).text
    print(aaa)
    proxy_host = aaa.strip()
    # proxy_host='1.193.175.60:10808'
    proxy = {

        'http': 'http://' + proxy_host,
        'https': 'https://' + proxy_host,
    }
    print(proxy)
    return proxy


if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    # url = 'http://202020.ip138.com'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)'
    }

    proxy = get_proxy(headers)
    r = requests.get(url, headers=headers, proxies=proxy, verify=False)
    print(r.text)

    url = 'https://httpbin.org/ip'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)'
    }

    r = requests.get(url, headers=headers, proxies=proxy, verify=False)
    print(r.text)
    print(proxy)
