#!/usr/bin/python3.7
#Filename:斐波那契数列的某个数.py

#计算斐波那契数列的第n个数

a = int(input("要求第几个斐波那契数："))

def fib(n):
    if n==1 or n==2:
        return 1    #return只在函数内使用，返回一个对象，但是不打印（需要print配合）
    elif n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)    #迭代函数

print(fib(a))
