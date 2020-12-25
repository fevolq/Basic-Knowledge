#python3.7
#Filename:findall的用法和非贪婪匹配.py

import re

a = '<a href="http://money.163.com/16/0425/14/BLGM1PH5002551G6.html" title="贾跃亭的成功意味着实体失败?" class="newsimg" lang="http://img2.cache.netease.com/stock/2016/4/25/20160425142754b9d8e_550.jpg"><img src="http://s.cimg.163.com/stock/2016/4/25/20160425142754b9d8e_550.jpg.119x83.jpg" alt="贾跃亭的成功意味着实体失败?"></a>,<a href="http://money.163.com/16/0422/15/BL90MCB400253G87.html" title="海尔模式为何在西方叫好不叫座" class="newsimg" lang="http://img1.cache.netease.com/stock/2016/4/22/2016042214244023f7e_550.png"><img src="http://s.cimg.163.com/stock/2016/4/22/2016042214244023f7e_550.png.119x83.jpg" alt="海尔模式为何在西方叫好不叫座"></a>   <span class="time">2016-04-25 14:28:18</span>  <span class="time">2016-04-12 15:30:49</span>'
reUrl = re.compile(r'href="(http.*?)"')
reTitle = re.compile(r'title="(.*?)"')
retime = re.compile(r'class="time">(\S+\s\S+)\d<')

pU = reUrl.findall(a)
pT = reTitle.findall(a)
pt = retime.findall(a)

print(pU)
print(pT)
print(pt)
