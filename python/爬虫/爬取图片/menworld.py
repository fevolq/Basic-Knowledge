#python3.7
#Filename:menworld.py

#待优化：异常处理

import requests
import os,time
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
def get_response(url):
    """返回网址的html"""
    response = requests.get(url,headers=headers)
    return response

def get_img(response):
    """找出需要的图片链接"""
    soup = BeautifulSoup(response.text,'html.parser')
    item_img = soup.select('#tFocus-pic img')
    for i in item_img:
        src = i['src']
        return src

def get_title(response):
    """返回当前图片系列的名称"""
    response.encoding = response.apparent_encoding  #避免中文乱码
    soup = BeautifulSoup(response.text,'html.parser')
    item_title = soup.select('.daohang a')
    for i in item_title:        #这个for循环待优化
        title = i.get_text()
    return title

def get_img_num(response):
    """返回当前图片系列一共有多少张图"""
    soup = BeautifulSoup(response.text,'html.parser')
    item_title = soup.select('.pagelist span')
    num = len(item_title)-2
    return num

def save(img_urls,path):    #将图片链接放到一个列表中
    """保存图片"""
    i = 1
    for img_url in img_urls:
        try:
            response = requests.get(img_url,headers=headers)
            with open(path+"{}.jpg".format(i),'wb') as f:
                f.write(response.content)
            print("{}已下载".format(img_url))
            i += 1
            time.sleep(1)
        except:
            print("{}下载错误".format(img_url))
            i += 1

def file(title):
    path = 'C:\\Users\\15394\\Desktop\\menworld\\'
    if os.path.exists(path+title) == False:
        path = path + title + r'\\'
        os.makedirs(path)
    else:
        path = path + title + r'\\'
    return path

def main(u):
    response = get_response(u+'.html')
    img_url = get_img(response)     #图片链接
    title = get_title(response)     #图片系列名称
    img_num = get_img_num(response)     #图片数量
    print('共{}张图片'.format(img_num))
    img_urls = [img_url]
    for page in range(2,img_num+1):
        url = u + '_{}.html'.format(page)
        response = get_response(url)
        img_url = get_img(response)
        img_urls.append(img_url)
        time.sleep(1)
    print("正在下载中")
    path = file(title)
    save(img_urls,path)
    
if __name__ == '__main__':
    #url = 'https://www.menworld.org/kjn1/16773.html'    
    #url = 'https://www.menworld.org/swmt1/13437.html'
    #url = 'https://www.menworld.org/ddtp/16718.html'
    url = 'https://www.menworld.org/lt/17565.html'
    u = url[0:-5]
    main(u)
    print('\nDone')
