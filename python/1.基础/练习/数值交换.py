#!/usr/bin/python3.7
#Filename:数值交换.py

#在不新增变量的情况下，将两个数值交换

class A: 
    x = 1
    y = 2
    print('x、y分别是%d—%d'%(x,y))
    def change(x,y):
        x,y = y,x
        print('x、y分别是%d—%d\n'%(x,y))

    x = 1
    y = 2
    change(x,y)

class B:
    a = 1
    b = 2
    print('a、b分别是%d—%d'%(a,b))
    a = a + b
    b = a - b
    a = a - b
    print('a、b分别是%d—%d\n'%(a,b))

class C:
    m = 1
    n = 2
    print('m、n分别是%d—%d'%(m,n))
    m = m ^ n
    n = m ^ n       #按位异或（二进制，对应位相同为0，不同为1）
    m = m ^ n
    print('m、n分别是%d—%d\n'%(m,n))
