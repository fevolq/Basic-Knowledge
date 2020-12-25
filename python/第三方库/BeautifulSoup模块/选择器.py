#python3.7
#Filename:选择器.py

from bs4 import BeautifulSoup

"""
标准选择器：
find_all(name,attrs,recursive,text,**kwargs)
可以根据标签名，属性，内容查找文档
以列表形式返回所有符合的
"""
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html,'html.parser')

#标签查找
def a():
    print(soup.find_all('ul'),'\n')
    print(type(soup.find_all('ul')[0]),'\n')
    for ul in soup.find_all('ul'):
        print(ul.find_all('li'),'\n')

def b():
    #attrs传入字典方式来查找标签
    print(soup.find_all(attrs={'id':'list-1'}),'\n')
    print(soup.find_all(attrs={'name':'elements'}),'\n')
    print(soup.find_all(attrs={'class':'element'}),'\n')   

def c():
    print(soup.find_all(text='Foo'))    #['Foo', 'Foo']，返回的是查到的所有的text='Foo'的文本


"""
css选择器：
.表示class #表示id
标签1，标签2 找到所有的标签1和标签2
标签1 标签2 找到标签1内部的所有的标签2
[attr] 可以通过这种方法找到具有某个属性的所有标签
[attr=value] 例子[target=_blank]表示查找所有target=_blank的标签
"""
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup = BeautifulSoup(html,'html.parser')
def d():
    print(soup.select('.panel .panel-heading'),'\n')
    print(soup.select('ul li'),'\n')
    print(soup.select('#list-2 .element'),'\n')
    print(type(soup.select('ul')[0]),'\n')

def e():    #利用get_text()获取内容
    print(soup.select('li'),'\n')
    for li in soup.select('li'):
        print(li.get_text(),'\n')    #获取文本内容

def f():    #利用[属性名]或attrs[属性名]来获取属性
    print(soup.select('ul'),'\n')
    for ul in soup.select('ul'):
        print(ul['id'])
        print(ul.attrs['id'],'\n')

if __name__ == '__main__':
    e()

"""
标签选择筛选功能弱但是速度快
建议使用find()、find_all() 查询匹配单个结果或者多个结果
如果对CSS选择器熟悉建议使用select()
记住常用的获取属性和文本值的方法
"""
