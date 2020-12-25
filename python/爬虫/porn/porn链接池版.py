#python3.7
#链接池抽取。链接池中，已完成的数据条中ny为Y，待爬取的数据条中ny为N。

#思考：将数据库函数都放到另一个文件
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

def other_urls(response):
    """当前页面查出的链接到其他页面的urls"""
    other_re = re.compile(r'<a class="js-thumb" href="(.*?)" title')
    l = re.findall(other_re,response)
    urls = []
    for url in l:
        url = "https://porninporn.com/" + url
        urls.append(url)
    return urls

def save(title,photo_id,photo_url):
    """保存图片"""
    path = "C:\\Users\\15394\\Desktop\\porn"
    if os.path.exists(path) == False:
        os.makedirs(path)
        path = path + r"\\"
    else:
        path = path + r"\\"
    photo_id = photo_id + 1
    try:
        photo_resp = resp(photo_url)
        with open(path+"{} {}.jpg".format(photo_id,title),"wb") as f:
            f.write(photo_resp.content)
            print("{}已下载".format(title))
    except:
        print("{}下载错误".format(title))
    return photo_id

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

def mysql_search():
    """查询最后一个使用的photo_id"""
    config = {
        "host":"127.0.0.1",
        "user":"root",
        "password":"mysql",
        "database":"pymysql"
        }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql_search_photo_id = "select photo_id from porn_name order by photo_id desc limit 1"
    try:
        cursor.execute(sql_search_photo_id)
        ids = cursor.fetchall()
        if len(ids) == 0:
            photo_id = 0
        else:
            photo_id = ids[0][0]
            photo_id = int(photo_id)
        db.close()
        return photo_id
    except:
        print("查询photo_id错误")
        db.close()
        return None

def insert_urls(urls):  #变量是一个列表
    """插入链接池处理：插入正则出的其他链接到数据库，已存在的不插入"""
    config = {
        "host":"localhost",
        "user":"root",
        "password":"mysql",
        "database":"pymysql"
        }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql_insert = "insert ignore into porn_urls_do (url,ny) values(%s,'N')"
    try:
        cursor.executemany(sql_insert,urls)
        db.commit()
    except:
        print("插入到链接池错误")
    db.close()

def update_urls(url):
    """更新链接池：将已爬取完成的链接对应的ny字段更改为Y"""
    config = {
        "host":"localhost",
        "user":"root",
        "password":"mysql",
        "database":"pymysql"
        }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql_update = "update porn_urls_do set ny='Y' where url=%s"
    try:
        cursor.execute(sql_update%url)
        db.commit()
    except:
        print("更新链接池错误")
    db.close()

def select_urls():
    """查询字段ny为N的数据条中的url字段，随机选取一个"""
    config = {
        "host":"localhost",
        "user":"root",
        "password":"mysql",
        "database":"pymysql"
        }
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql_search = "select url from test as t1 join (select round(rand()*(select max(id) from test)) as id) as t2 where t1.id>=t2.id and t1.ny='N' order by t1.id limit 1"
    try:
        cursor.execute(sql_search)
        result = cursor.fetchall()
        url = result[0][0]
        db.close()
        return url
    except:
        print("查询数据库，取出链接失败")
        db.close()
        return None

def main(url):
    """运行步骤"""
    #确定photo_id
    photo_id = mysql_search()   #最后一次使用的photo_id
    
    response = resp(url)
    l = download(response.text)
    title = l[0][0]
    photo_url = l[1][0]
    source_url = l[2][0]
    urls = other_urls(response.text)     #其他链接（待入链接池）

    try:
        insert_urls(urls)   #插入正则出的其他链接到链接池
        photo_id = save(title,photo_id,photo_url)   #保存文件
        mysql_insert(title,photo_id,photo_url,source_url,url)   #插入数据库
        update_urls(url)    #更新链接池（更新ny字段）
        url = select_urls()     #从链接池随机抽取的下一个要爬取的链接
    except:
        print("Error")
    time.sleep(1)
    main(url)

if __name__ == '__main__':
    url = "https://porninporn.com/show/play/ph5cc2dd3b4e87a/japanese-sister-playing-with-her-sister-s-breasts"
    photo_id = mysql_search()
    try:
        if photo_id == 0:   #若是第一次运行，则将此url插入到链接池
            urls = [url]
            insert_urls(urls)
        else:
            url = select_urls()   #若是断点续传，则此时的url早已完成了爬虫，需重新定向url
        print("开始运行")
        print("url=",url)
        main(url)
    except:
        print("main错误")

"""
待解决：
1.最初运行的第一个链接，要先插入到链接池。
2.断点续传：photo_id问题已解决。第一个url的选取问题。

思路：
增加一个if语句，放在末尾的if中，条件是photo_id的查询函数返回的是否为0
是，则代表程序是第一次运行，加一个命令：将此url插入到链接池
否，则代表程序是断点续传，加一个命令：将url重新定向为从链接池随机抽取的链接

已解决
"""



















