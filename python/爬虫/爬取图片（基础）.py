#python3.7
#Filename:爬取图片.py

import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
resp = requests.get("http://www.baidu.com/img/baidu_jgylogo3.gif",headers=headers)
print(resp.content)        #二进制文件用content

#保存图片
with open("图片.gif","wb") as f:
    f.write(resp.content)
    #print("ok")

    
