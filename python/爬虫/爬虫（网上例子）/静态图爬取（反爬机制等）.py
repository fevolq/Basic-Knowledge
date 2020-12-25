# 导入相关的库
import requests
from bs4 import BeautifulSoup
import os
 
# 待爬取的网址
all_url = 'http://www.mzitu.com'
 
 
# http请求头，防止反爬虫
Hostreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'
               }
# 此请求头破解盗链
Picreferer = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://i.meizitu.net'
}
 
# 解析页面
start_html = requests.get(all_url,headers = Hostreferer)
 
# 爬取图片的保存地址
path = 'C:\\Users\\15394\\Desktop\\静态图爬取\\'
 
#找寻最大页数
soup = BeautifulSoup(start_html.text,"html.parser")
page = soup.find_all('a',class_='page-numbers')
max_page = page[-2].text

same_url = 'http://www.mzitu.com/page/'
# 逐个爬取套图
for n in range(1,int(max_page)+1):
    ul = same_url+str(n)
    # 解析页面
    start_html = requests.get(ul, headers = Hostreferer)
    soup = BeautifulSoup(start_html.text,"html.parser")
    # 找到图片所在的位置
    all_a = soup.find('div',class_='postlist').find_all('a',target='_blank')
    for a in all_a:
        title = a.get_text()    #提取文本
        #print(title)
        if(title != ''):
            print("准备扒取："+title)
 
            # win不能创建带？的目录
            if(os.path.exists(path+title.strip().replace('?',''))):
                    #print('目录已存在')
                    flag=1
            else:
                os.makedirs(path+title.strip().replace('?',''))
                flag=0
            os.chdir(path + title.strip().replace('?',''))
            
            # 找到href属性信息
            href = a['href']
            html = requests.get(href,headers = Hostreferer)
            mess = BeautifulSoup(html.text,"html.parser")
            pic_max = mess.find_all('span')
            pic_max = pic_max[10].text          #最大页数
            if(flag == 1 and len(os.listdir(path+title.strip().replace('?',''))) >= int(pic_max)):
                print('已经保存完毕，跳过')
                continue
 
            # 爬取套图中每一页的图片
            for num in range(1,int(pic_max)+1):
                pic = href+'/'+str(num)
                html = requests.get(pic,headers = Hostreferer)
                mess = BeautifulSoup(html.text,"html.parser")
                pic_url = mess.find('img',alt = title)
                print(pic_url['src'])
                #exit(0)
                html = requests.get(pic_url['src'],headers = Picreferer)
                file_name = pic_url['src'].split(r'/')[-1]
                
                # 保存结果
                f = open(file_name,'wb')
                f.write(html.content)
                f.close()
            print('完成')
    print('第',n,'页完成')

