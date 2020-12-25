#python3.7
#Filename:爬取小说.py

#包含乱码问题、替换字符问题、输出换行问题等

#后续处理：进程问题、异常处理

import requests,re,os

def get_response(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding    #乱码问题，很关键
    return response

def get_allurls(response):
    url_Re = re.compile(r'<dd><a href="(.*?)">(.*)</a></dd>')
    urls = url_Re.findall(response.text)   #所有章节的地址     re.findall(url_Re,response.text)
    return urls

def download_txt(response):
    title_Re = re.compile(r'var readtitle = "(.*?)";')    #章节名
    title = title_Re.findall(response.text)
    txt_Re = re.compile(r'<div id="content">(.*?)</p></div>',re.S)    #正文
    txt = txt_Re.findall(response.text)
    return title[0],txt[0]

def save(title,txt):
    path = os.getcwd()
    path = path+"\\修真聊天群\\"
    if os.path.exists(path) == True:
        pass
    else:
        os.makedirs(path)
    with open(path+"{}.txt".format(title),"wb") as f:    #单章单文件，wb重写
            f.write(title.encode("gbk"))
            txt = txt.replace("&nbsp;","\r\n")
            txt = txt.replace("<p>","\r\n")
            txt = txt.replace("</p>","\r\n")    #windows下的写入换行时，\r\n
            txt = txt.replace("www.31xs.com","")
            f.write(txt.encode("gb18030"))    #写入正文时的转码（由于原网站是gbk格式的编码），gb18030避免文内有些特殊字符不能转义
    with open("C://Users//15394//Desktop//修真聊天群.txt","ab") as f:   #所有章节单文件，ab追加
            f.write(title.encode("gbk"))
            txt = txt.replace("&nbsp;","\r\n")
            txt = txt.replace("<p>","\r\n")
            txt = txt.replace("</p>","\r\n")    #windows下的写入换行时，\r\n
            txt = txt.replace("www.31xs.com","")
            f.write(txt.encode("gb18030"))
            f.write("\r\n\r\n\r\n".encode("gbk"))
    print("{}  已下载".format(title))

def main():
    start_url = "http://www.31xsw.com/0/160/"     #小说页面——编码形式为gbk
    start_response = get_response(start_url)
    urls = get_allurls(start_response)
    for url in urls[11:]:
        txt_url = "http://www.x31xs.org" + url[0]
        txt_response = get_response(txt_url)
        title = download_txt(txt_response)[0]
        txt = download_txt(txt_response)[1]
        save(title,txt)

if __name__ == "__main__":
    print("单章版存于当前工作目录下，合集版存于桌面")
    try:
        main()
        print("Done")
    except:
        print("异常")

#乱码问题：在requests获取response后，先response.encoding = response.apparent_encoding，再使用response.text
