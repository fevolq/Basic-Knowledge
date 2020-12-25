#!/usr/bin/python3.7
#Filename:文本对齐.py

#rjust(x)选择x长度的字符串，在里面将提供的字符右对齐，前面填充空格
print("hello".rjust(10),"\n")
#print("1",end=",")
print("hello".rjust(20),"\n")


print("\n")

print("hello".rjust(10,"*"),"\n")   #将*填充在前面
print("hello".rjust(20,"9"),"\n")

print("hello".ljust(10,"*"),"\n")   #将*填充在后面
print("hello".ljust(20,"9"),"\n")

print("\n")

#center()居中对齐
print("hello".center(10))
print("hello".center(20))

print("hello".center(10,"9"))   #填充物（“9”）必须是单字符
print("hello".center(20,"+"))       #若无法刚好居中，则右边比左边多一个字符

#填充物为单字符
