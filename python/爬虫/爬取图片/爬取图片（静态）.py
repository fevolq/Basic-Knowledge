#python3.7
#Filename:爬取图片.py

import requests,re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
url = "http://hbimg.huabanimg.com/4b31e87efa600a5733a6330b87b8805f189cb447fd86-nQfLmM_fw658"    #直接使用了图片所在的网址
url_get = requests.get(url,headers=headers)
#print(url_get.text)        #二进制文件用content
"""
正则
url_Re = re.compile(r'<img src="(.*?)" width="658"')
url_img = url_Re.findall(url_get.text)
print(url_img)
#img = requests.get(url_img[0][0],headers=headers)
"""
#保存图片
with open("图片.png","ab") as f:
    f.write(url_get.content)    #二进制文件保存（图片音乐视频等）时用content

print("ok")

#https://huaban.com/pins/2353890738/    #使用此网址时，返回的信息内没有图片的网址信息，无法进行正则。（该网址为动态）
#http://hbimg.huabanimg.com/4b31e87efa600a5733a6330b87b8805f189cb447fd86-nQfLmM_fw658   #静态


#直接在图片的网址进行爬取，所以不需要使用正则
