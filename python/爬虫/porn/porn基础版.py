#python3.7
#单个网址页面的爬取

#单个网址页面的爬取，且没有返回链接到其他页面的链接
#待优化：异常处理

import requests,pymysql
import os,re,time

def resp(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response
    else:
        print("网址请求错误")
        return None

def download(response):
    """找出图片名，图片地址，视频链接"""
    title_re = re.compile(r'<h1 class="videoTitle">(.*?)</h1>')
    photo_re = re.compile(r'poster="(.*?)"')
    source_re = re.compile(r'<source src="(.*?)" type="video/mp4" data-res')
    title = re.findall(title_re,response)
    photo = re.findall(photo_re,response)
    source = re.findall(source_re,response)
    #print(title,"\n",photo,"\n",source)
    return title,photo,source

def save(title,photo_id,photo_url):
    """保存图片"""
    path = "C:\\Users\\15394\\Desktop\\porn"
    if os.path.exists(path) == False:
        os.makedirs(path)
        path = path + r"\\"
    else:
        path = path + r"\\"
    try:
        photo_resp = resp(photo_url)
        with open(path+"{} {}.jpg".format(photo_id,title),"wb") as f:
            f.write(photo_resp.content)
            print("{}已下载".format(title))
    except:
        print("{}下载错误".format(title))

def mysql_insert(title,photo_id,photo_url,source_url,face_url):
    """插入数据库"""
    config = {
        "host":"127.0.0.1",
        "user":"root",
        "password":"mysql",
        "database":"pymysql"
        }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    try:
        sql_insert_1 = "insert into porn_name(title,photo_id) values(%s,%s)"
        cursor.execute(sql_insert_1,(title,photo_id))
        db.commit()
    except:
        sql_insert_2 = "insert into porn_name(title,photo_id) values(%s,%s)"
        cursor.execute(sql_insert_2,("error",photo_id))
        db.commit()
        print("图片{}插入title到数据库错误".format(photo_id))
    try:
        sql_insert_3 = "insert into porn_url(photo_id,photo_url,source_url,face_url) values(%s,%s,%s,%s)"
        cursor.execute(sql_insert_3,(photo_id,photo_url,source_url,face_url))
        db.commit()
    except:
        sql_insert_4 = "insert into porn_url(photo_id,photo_url,source_url,face_url) values(%s,%s,%s,%s)"
        cursor.execute(sql_insert_3,(photo_id,"error","error","error"))
        db.commit()
        print("图片{}插入url到数据库错误".format(photo_id))
    db.close()

def main():
    """运行步骤"""
    url = "https://porninporn.com/show/play/ph5cc2dd3b4e87a/japanese-sister-playing-with-her-sister-s-breasts"
    #url1 = "https://porninporn.com/show/play/ph5cc06e866bebc/japanese-hostess-and-her-maid"
    response = resp(url)
    l = download(response.text)
    #print(l[0][0])
    title = l[0][0]
    photo_url = l[1][0]
    source_url = l[2][0]
    photo_id = 1
    try:
        save(title,photo_id,photo_url)
        mysql_insert(title,photo_id,photo_url,source_url,url)
    except:
        print("Error")

if __name__ == '__main__':
    try:
        main()
        time.sleep(1)
    except:
        print("main错误")
























