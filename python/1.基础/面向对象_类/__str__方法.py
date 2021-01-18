#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:2021.01.17
# Filename:类之中的__str__(self)的用法

class test(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __A(self):  #前面加上双下划线，就变成了类的私有方法，只能在类内调用这个方法，无法在外部使用
        c = self.a + self.b
        print('c是：',c)
        return c

    def start(self):
        s = self.__A() + 1
        return s

    def __str__(self):
        print('这里是__str__方法')
        return '输入的第一个为：%s,\n第二个数为：%s'%(self.a,self.b)

t = test(1,2)
# print(t.__A())    #错误，无法调用类的私有方法。
print(t.start(),'\n')
# print(t.start,'\n')

print(t)
###t代表了test()这个对象，当对象中使用了__str__(self)这个方法时，
# 一旦使用print打印这个对象，就会打印__str__方法中return的数据。
###__str__方法需要返回一个字符串，当作这个对象的描写。
