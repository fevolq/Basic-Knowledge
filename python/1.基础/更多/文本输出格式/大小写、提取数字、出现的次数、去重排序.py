#!/usr/bin/python3.7
#Filename:大小写、提取数字、出现的次数、去重排序.py

#大小写
print("大小写：")
a = "Hello"

print(a.upper())    #将所有字母以大写返回
print(a.lower())    #将所有字母以小写返回
print(a.swapcase())     #将字母大小写反转

print("\n")

print(a.isupper())  #判断是否全为大写（返回True  False）
print(a.upper().isupper())
print(a.lower().isupper())
print(a.upper().lower()) #变成大写再变成小写


#提取数字
print("\n提取数字：")
a = "asd123QWE987"

print(" ".join(i for i in a if i.isdigit()))

b = "123456"
c = 123456
print(a.isdigit())      #判断字符串内是否全部都是数字
print(b.isdigit())
#print(c.isdigit())——异常


#出现的次数
print("\n出现的次数：")
a = "abc15bcdfaaaf1"

print(a.count("f"))     #返回f出现的次数
print(dict([(i,a.count(i)) for i in set(a)]))     #将a内每个元素出现的次数呈字典形式返回，set()集合（去重）
                                                 #注意如何将元组变成字典dict([(x,y)])


#将字符串去重按顺序重新排列
print("\n将字符串去重按顺序重新排列：")
a = "abc15bcdfaaaf1"
b = list(a)
#print(b)
c = set(b)      #集合去重
d = list(c)         #变为列表
d.sort(key=b.index)     #按原先顺序排列
print("".join(d))   #输出成字符串
