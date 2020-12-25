#python3.7
#Filename:功能预览.py

import requests
from bs4 import BeautifulSoup

star_url = "https://www.mzitu.com/176425"
headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}

response = requests.get(star_url)

#使用BeautifulSoup
soup = BeautifulSoup(response.text,"html.parser")   #使用的是html.parser模式

a0 = soup.find("meta")  #找出首个"meta"行
a1 = soup.find_all("meta")  #找出所有"meta"行，以列表形式返回
#print(a0,"\n\n",a1)

b = soup.find("title")
b0 = soup.find("title").string  #将其内的内容以字符串形式返回
b1 = b.string
b2 = soup.head.title.string    #层层迭代的嵌套查找
#print(b0,"\n\n",b1,"\n\n",b2)

#子(孙)节点，父节点
c0 = soup.body.ul.contents  #获取子节点（使用contents），返回的列表中，每个换行符也占一个元素
#print(c0)
#c1 = soup.body.ul.children     #children也是获取子节点，但它是一个迭代器，使用方法不同
c2 = soup.ul.parent     #获取父节点（使用parent），按行返回
#print(c2)

#关键标签查找
d0 = soup.find_all(attrs={"class":"logo"})  #使用attrs传入字典进行精确查找
d1 = soup.find("ul").find_all(attrs={"title":"日本妹子"})   #多次使用时，find在前，find_all在后
d2 = soup.find_all(attrs={"title":"日本妹子"})
d3 = soup.find_all(title="日本妹子")    #(简洁化attrs),使用标签，在使用class标签时，要加下划线(即class_)
#print(d0,"\n\n",d1,"\n\n",d2,"\n\n",d3)

#CSS选择器
e0 = soup.select("ul li")   #选择ul标签内的li标签（以空格分离），以列表形式返回
e1 = soup.select(".header h1")  #选择class="header"内的h1标签，class的用法(以点号开头，后跟class的值)
e2 = soup.select(".mainnav #menu-nav")  #选择class="mainnav"内的id="menu-nav"所属逻辑标签，id的用法(以#开头，后跟id的值)
e3 = soup.select("li a")    #或soup.find("ul").find_all("a")
print(e0,"\n\n",e1,"\n\n",e2,"\n\n",e3)
print("\n")

#获取需要的内容
for i in e0:
    f0 = i.get_text()   #获取未命名的内容
    print(f0)
for x in e1:
    f1 = x["class"]     #这里不能获取"href" 
    print(f1)
for y in e3:
    f3 = y["href"]      #获取标签内容
    f4 = y["title"]
    print(f3,f4)

print(soup.find("ul").find_all("a"))
