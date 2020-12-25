#!/usr/bin/python3.7
#Filename:集合.py

#删除重复元素，进行成员测试

s = {"a","b",1,2,6,2,"b"}   #集合可用{}或set()创建，但空集合只能用set()创建

print(s,"\n")                    #消除重复元素

if "b" in s:                #成员测试
    print("True")
else:
    print("False")

print("")

def x():
    m = set("abcdefg")
    n = set("acejkl")

    a = m - n           #在m中，但不在n中
    print(a,"\n")

    b = m | n           #在m或n中
    print(b,"\n")

    c = m & n           #在m和n中都有
    print(c,"\n")

    d = m ^ n           #不同时在m和n中
    print(d,"\n")

x()

a1 = set("qwertwe")     #set创建集合时，只能包含一个字符串，且返回时会拆分成单个字符
a2 = set("qwe,tw")
print(a1,a2)


