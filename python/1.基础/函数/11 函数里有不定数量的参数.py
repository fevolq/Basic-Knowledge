#!/usr/bin/python3.7
#Filename:函数里有不定数量的参数.py

class list():
    """
    *args主要用于函数定义，可以将不定数量的参数传递给一个函数。
    *args用来发送一个非键值对的可变数量的参数列表给一个函数，以元组形式导入。
    """
    def m(args_f,*args):
        print("\n",args_f)
        print(args)
        print(type(args))
        print(i for i in args)
        for i in args:
            print(i)

    m(8)
    m("a","b","c",1)

print("\n\n")

class key_value():
    """
    **args允许将不定长度的键值对，作为参数传给一个函数，以字典形式导入。
    """
    def n(**args_v):
        print(type(args_v))
        print(args_v)

    n(q="w")    #注意使用的表达方法
    n(a = 1,b= 2)

