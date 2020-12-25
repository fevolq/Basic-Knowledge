#!/usr/bin/python3.7
#Filename:compile函数.py

#compile函数用于编译正则表达式，生成一个正则表达式对象，供match()和search()使用

import re

com = re.compile(r'\d+')      #\d+匹配一个或多个数字

a = com.match("asd12sad59fs")  #查找头部，没有
print(a)

b = com.match("asd12sad59fs",2,10)  #表示从“d”的位置开始匹配到“f”的位置
print(b)

c = com.match("asd12sad59fs",3,10)  #从“1”的位置开始匹配
print(c)        #返回一个match对象

print(c.group(0)," ",c.start(0),"",c.end(0),"",c.span(0))     #可省略0，后面3个操作用于表示匹配字符的位置

#语法：re.compile(pattern[,flags])
#pattern:一个字符串形式的正则表达式，即需要匹配出什么
#flags：可选，表示匹配模式。具体参数如下：
"""
re.I忽略大小写
re.L表示特殊字符集\w,\W,\b,\B,\s,\S依赖于当前环境
re.M多行模式
re.U表示特殊字符集\w,\W,\b,\B,\s,\S依赖于Unicode字符属性数据库
re.X为了增加可读性，忽略空格和#后面的注释
"""
print("")

example = re.compile(r"abc",re.I)     #re.I作为第二个参数，表示匹配的时候忽略正则表达式中的大小写。
d1 = example.search("yjhuabcjdifaBC")   #查找首个匹配的
d2 = example.search("goJABCko")
d3 = example.search("fhAbCjfo")
d4 = example.findall("fhuaBcjfoABCHFIO")    #查找出所有符合的匹配，以列表形式返回
print("d1的匹配：",d1.group(),"\nd2的匹配：",d2.group(),"\nd3的匹配：",d3.group(),"\nd4的匹配：",d4)
