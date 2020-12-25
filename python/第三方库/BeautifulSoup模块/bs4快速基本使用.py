#python3.7
#Filename:bs4快速基本使用.py

from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
soup = BeautifulSoup(html,'html.parser')    #使用的是python（内置）标准库的解析器，所以使用'html.parser'方法
"""
print(soup.prettify(),"\n")     #将内容按层次进行划分
print(soup.title,"\n")      #<title>The Dormouse's story</title>
print(soup.title.name,"\n")     #title
print(soup.title.string,"\n")   #The Dormouse's story
print(soup.title.parent.name,"\n")  #head，返回title的上一层的名字
print(soup.p,"\n")      #<p class="title"><b>The Dormouse's story</b></p>，返回首个p标签
print(soup.p["class"],"\n")     #['title']，返回p标签内class的值
print(soup.a,"\n")      #<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
print(soup.find_all('a'),"\n")      #以列表形式返回所有a标签
print(soup.find(id='link3'),"\n")   #<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>，返回符合的标签
"""
for link in soup.find_all('a'):
    print(link.get('href'))     #得到a标签内的href的值

print(soup.get_text())  #返回所有文字内容（即没有对应的键）

"""
标签选择器:
在快速使用中我们添加如下代码：
print(soup.title)
print(type(soup.title))
print(soup.head)
print(soup.p)
通过这种soup.标签名 我们就可以获得这个标签的内容
这里有个问题需要注意，通过这种方式获取标签，如果文档中有多个这样的标签，返回的结果是第一个标签的内容，如上面我们通过soup.p获取p标签，而文档中有多个p标签，但是只返回了第一个p标签内容

获取名称:
当我们通过soup.title.name的时候就可以获得该title标签的名称，即title

获取属性:
print(soup.p.attrs['name'])
print(soup.p['name'])
上面两种方式都可以获取p标签的name属性值

获取内容:
print(soup.p.string)
结果就可以获取第一个p标签的内容：
The Dormouse's story

嵌套选择:
我们直接可以通过下面嵌套的方式获取
print(soup.head.title.string)
"""
