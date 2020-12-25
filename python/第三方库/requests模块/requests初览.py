#python3.7
#Filename:requests初览.py

import requests

#requests.get()函数需要一个url字符串才能下载，返回一个response对象
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")   #下载网页（内容）

class A1:
    print("A1:")
    print(res)
    print(type(res))
    res.status_code == requests.codes.ok        #通过检查status_code属性来判断网页请求是否成功
                                             #若成功，则下载的网页将作为字符串存储在response对象的text变量中
    print(len(res.text))        #显示存储的对象的字符长度
    print(res.text[:250])       #返回存储在text内的内容到显示屏上（即网页上下载的内容）


print()  
class A2:   #判断是否异常
    print("A2:")
    try:                            
        res.raise_for_status()          #raise_for_status()方法是确保程序在发生错误下载时停止的办法
        #print("正常")
    except Exception as exc:
        print("有异常：%s"%(exc))


print()
class A3:
    print("A3:")
    res.raise_for_status()      #判断下载是否错误
    playFile = open("123.txt","wb")     #打开(写入)文件
    for resunk in res.iter_content(10000):      #iter_content()方法通过循环迭代返回块中的内容，可指定每个块将包含多少字节
        playFile.write(resunk)
    playFile.close()

print("\nDone")
