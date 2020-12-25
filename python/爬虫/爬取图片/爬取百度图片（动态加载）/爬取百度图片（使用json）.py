#python3.7
#Filename:爬取百度图片（动态加载，使用jsoon）.py
# coding = utf-8

import os,re
import requests,json

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
    #print(params)
    url = 'https://image.baidu.com/search/acjson'   #使用的是浏览器的"Request URL"，注意搜索的网址（acjson后缀）
    urls = []
    for i in params:
        re_get = requests.get(url,params=i)     #注意params（进行动态加载）的使用方法
        #print(re_get.text)

        #json的使用
        l = json.loads(re_get.text)     #注意json的使用方法或l=re_get.json()
        #print(l)
        l = l['data']       #返回的json数据中关键字
        #print(l)
        
        urls.append(l)
    #print(urls)   
    return urls,keyword

def getImg(datalist,name,path="C:\\Users\\15394\\Desktop\\默认\\"):
    if os.path.exists(path+name) == False:   #指定保存的位置
        path = path + name + r"\\"
        os.makedirs(path)
    else:
        path = path + name + r"\\"
    x=1
    for list in datalist:
        for i in list:
            if i.get('thumbURL') != None:       #单个图片的地址为i.get('thumbURL')
                print('正在下载：%s' % i.get('thumbURL'))
                a = requests.get(i.get('thumbURL'))
                with open(path+"{}{}.jpg".format(name,x),"wb") as f:
                    f.write(a.content)
                x += 1
            else:
                print('图片链接不存在')
 

a = input("请输入想要查找的图片的姓名：")
b = int(input("请输入想要查找的组数（一组30张）："))
path = input("请输入想要保存的地址（如：（回车默认）保存到桌面C:\\Users\\15394\\Desktop\\）：")
if __name__ == '__main__':
    getdatas = getDatas(a,b)
    datalist = getdatas[0]
    name = getdatas[1]
    if len(path) == 0:
        getImg(datalist,name)
    else:
        getImg(datalist,name,path)

print("Done")

#C:\\Users\\15394\\Desktop\\python教程\\python\\爬虫\\爬取图片\\爬取百度图片（动态加载）\\使用json\\
#C:\\Users\\15394\\Desktop\\图片\\

"""
word:搜索关键字，要用URL Encode,即非字母字符被替换成%后加两位十六进制数；

pn：每次递增30，每次异步请求可加载30张图片；

gsm: pn的十六进制值;

发现一张图片有4种URL：fromURL,middleURL,thumbURL,objURL,前三种有反爬措施，因此采用objURL
"""
