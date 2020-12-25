#python3.7
# coding = utf-8
#Filename:爬取百度图片（动态加载，使用正则）.py

import re,os
import requests

headers = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36" 
def getDatas(keyword,pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp':'result',
                      'queryWord':keyword,
                      'cl': 2,
                      'lm': -1,
                      'hd':'',
                      'latest':'',
                      'copyright':'',
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': '',
                      'istype': 2,
                      'qc':'',
                      'nc':1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': hex(i)[2:],
                      '1554623100183':''
                  })
    url = 'https://image.baidu.com/search/index'    #使用的是浏览器的"Referer"，注意与使用json时的不同
    urls = []
    #print(params)
    for i in params:
        re_get = requests.get(url,params=i)
        urls.append(re_get)
        #print(re_get)
    return urls,keyword
 

def get_img(datalist,name,path):      #使用的正则
    if os.path.exists(path+name) == False:   #指定保存的位置
        path = path + name + r"\\"
        os.makedirs(path)
    else:
        path = path + name + r"\\"
    x = 1
    for url in datalist:
        url_Re = re.compile(r'"thumbURL":"(.*?)"')
        img_urls = url_Re.findall(url.text)
        #print(img_urls)
        for img_url in img_urls:
            img = requests.get(img_url)
            with open(path+"{}{}.jpg".format(name,x),"wb") as f:
                f.write(img.content)
            x += 1
    
    
 
if __name__ == '__main__':
    getdatas = getDatas('陈钰琪',2)
    datalist = getdatas[0]
    name = getdatas[1]
    #getImg(datalist,'C://User//15394//Desktop//123//')
    get_img(datalist,name,'C:\\Users\\15394\\Desktop\\python教程\\python\\爬虫\\爬取图片\\爬取百度图片（动态加载）\\使用正则\\')

print("Done")
