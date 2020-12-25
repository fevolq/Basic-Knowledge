#!/usr/bin/python3.7
#Filename:正则表达式初览.py

import re
 
class match1:       #头部查找匹配
    '''
    re.match尝试从字符串的 起始位置 匹配一个模式。起始位置匹配不成功，则返回None。
    函数语法：re.match(匹配的正则表达式, 要匹配的字符串, 标志位（用于控制匹配方式）)
    '''
    print(re.match("as","asdfg.zxc").span())    #在起始位置匹配        返回匹配的位置
    print(re.match("fg","asdfg.zxc"))   #不在起始位置匹配

    line = "Cats are smarter than dogs"
    # .*表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
    match = re.match(r"(.*) are (.*) .*",line, re.M|re.I)

    #使用group(num)或groups()来获取匹配出的表达式
    #num=0，则返回整个正则表达式匹配的字符串。group()可以一次输入多个组号，这时它将返回一个包含那些组所对应值的元组。
    if match:
        print("match.group():",match.group())    
        print("match.group(1):",match.group(1))     #匹配正则表达式中的组是从1开始
        print("match.group(2):",match.group(2))       #贪婪匹配
        print("match.group(0):",match.group(0))     #上面的正则表达式里只有两个组，所以不能超过3
    else:
        print("没有匹配")


print("\n\n")

class search1:      #全文查找匹配
    '''
    re.search扫描整个字符串并返回第一个成功的匹配。匹配成功，返回对象。否则返回None。
    语法：re.search(匹配的正则表达式, 要匹配的字符串, 标志位（用于控制匹配方式）)
    '''
    line = "Cats are smarter than dogs"
    search = re.search(r"(.*) are (.*?) .*", line, re.M|re.I)

    if search:
        print("search.group():",search.group())
        print("search.group(1):",search.group(1))
        print("search.group(2):",search.group(2))   #非贪婪匹配
        print("search.group(1,2):",search.group(1,2))
    else:
        print("没找到")

print("\n\n")

class sub1:         #全文查找替换
    '''
    语法re.sub(pattern,repl,str,count=0)——用于替换字符串中的匹配项
    pattern:正则中的模式字符串，即正则表达式
    repl:替换的字符串，也可为一个函数
    str:要被查找替换的原始字符串
    count:匹配后替换的最大次数，默认0表示替换所有匹配
    '''
    phone = "123-456-789 # 这是一个电话号码"
    num = re.sub(r"#.*$","",phone)  #删除注释（从#开始，“.*”表示匹配出换行符的任何单个或多个字符，$表示匹配到结尾）
    print("电话号码：",num)

    num = re.sub(r"\D","",phone)    #移除非数字内容
    print("电话号码：",num)

    example = re.compile(r"has \w+")    #\w+表示任意个字母数字或下划线（除了空格和换行符）
    num = example.sub("loves","he has an apple.")
    print("num的匹配替换：",num)
    #"""
    example = re.compile(r"Agent (\w)\w*")
    num = example.sub(r"\****","Agent Alice told Agent Carol that Agent \
Eve knew Agent Bob was a double agent.")
    print("num的匹配替换：",num)
    #"""

class sliter:   #切割
    a = "a1b2c3d4"
    b = "a1b2c3d4e"
    m = re.split(r"\d",a)       #去除字符串内的数字
    n = re.split(r"\d",b)
    print("切割:",m,n)
