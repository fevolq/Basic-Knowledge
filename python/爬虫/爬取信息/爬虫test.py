#python3.7
#Filename:爬虫1.py

#爬取网页上的某些信息
#按照[{"title":title,"time":time,"url":url}，......]方式返回

import requests,re

res = requests.get("http://money.163.com/special/pinglun/")
#正则
"""
reClass = re.compile(r'<div class="list_item clearfix">.*</div>$')
_class = reClass.findall(res.text[:])
print(_class)
"""
reUrl = re.compile(r'href="(http://money.163.*?)" title')    
reTitle = re.compile(r'href=".*?" title="(.*?)" class')  
reTime = re.compile(r'class="time">(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})</span>')

#将需要的信息利用正则分类成列表
_title = reTitle.findall(res.text[:])   #注意：如何使用爬去过来的网页信息res.text[:]
#print(_title)
_url = reUrl.findall(res.text[:])
#print(_url)
_time = reTime.findall(res.text[:])
#print(_time)

#依次对应迭代
l = []
for i in range(len(_title)-2):
    s_title = dict([("title",_title[i])])
    s_time = dict([("time",_time[i])])
    s_url = dict([("url",_url[i])])
    s_title.update(s_time)
    s_title.update(s_url)
    
    l.append(s_title)
    del s_title,s_time,s_url

print(l)


