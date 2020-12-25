#!/usr/bin/python3.7
#Filename:嵌套函数作用域（非全局作用域）.py

#Enclosing（闭包函数外的函数中）
#nonlocal关键字（用法类似于global）

def func1():
    num = 0
    print("调用fun2之前，fun1函数中的num：",num,id(num))
    def func():         #函数内嵌套的函数
        #nonlocal num    
        num = 1
        print("fun2函数内的num：",num,id(num))
    func()              #在函数fun1中调用她的嵌套函数func
    print("调用fun2之后，fun1函数中的num：",num,id(num))

func1()          #调用最外层的函数fun1(),进行运行。

print("\n\n")

def func2():
    num = 0
    print("调用fun2之前，fun1函数中的num：",num,id(num))
    def func():         #函数内嵌套的函数
        nonlocal num    #利用nonlocal关键字声明num变量可以作用于此函数外的一个函数
        num = 1
        print("fun2函数内的num：",num,id(num))
    func()              #在函数fun1中调用她的嵌套函数func
    print("调用fun2之后，fun1函数中的num：",num,id(num))

func2()
