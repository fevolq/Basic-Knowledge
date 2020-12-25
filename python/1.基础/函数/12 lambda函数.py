#!/usr/bin/python3.7
#Filename:lambda函数.py

#lambda的语法：lambda arg1,arg2,......:逻辑表达式

sum = lambda arg1,arg2:arg1+arg2

print(sum(10,20))       #注意调用lambda函数的方法

a = sum(5,6)
print(a)


#用lambda函数来创建匿名函数。
#lambda的主体只是一个逻辑表达式，不是代码块，仅能封装有限的逻辑。
#lambda函数拥有自己的命名空间，但不能访问自己参数列表外或全局命名空间的参数。

print()

b = lambda x:x+1 if x>0 else "错误"   #不能使用for和while
print(b(6))
print(b(-6))

li = [1,2,3,4,5,6]
c = filter(lambda x:x>3,li)
print(type(c))
print(list(c))
