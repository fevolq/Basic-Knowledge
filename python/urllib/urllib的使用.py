#python3.7
#Filename:urllib的使用.py

"""
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
urllib.requeset.urlopen(url,data,timeout)
"""
    
def a():
    import urllib.request
    response = urllib.request.urlopen('http://www.baidu.com')
    print(response)
    #print(response.read())     #获取网页内容
    print(response.read().decode('utf-8'))
    
    """
response.read()可以获取到网页的内容
    """

def b():    #post请求
    import urllib.request
    import urllib.parse
    data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
    print(data)
    response = urllib.request.urlopen('http://httpbin.org/post',data=data)
    print(response.read())
    """
通过bytes(urllib.parse.urlencode())可以将post数据进行转换放到urllib.request.urlopen的data参数中。这样就完成了一次post请求。
所以如果我们添加data参数的时候就是以post请求方式请求，如果没有data参数就是get请求方式
    """
def c():    #设置(请求)超时时间，避免让程序一直在等待结果
    import urllib.request
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
    print(response.read())
    return response
def c1():   #对c函数的异常抓取
    import socket
    import urllib.error
    try:
        c()
        print('成功')
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('Time Out')

def d():    #响应类型、响应头、状态码
    import urllib.request
    response = urllib.request.urlopen('https://www.python.org')
    print(type(response))   #响应类型
    print(response.status)  #状态码
    print(response.getheaders().response.getheader("server"))   #获取头部信息

def e():    #添加请求头
    import urllib.request, urllib.parse
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
                }
    dict = {
       'name': 'zhaofan'
            }
    data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    #或req = urllib.request.Request(url=url, data=data, method='POST')
    #  req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))

if __name__ == '__main__':
    e()
    print('Done')
