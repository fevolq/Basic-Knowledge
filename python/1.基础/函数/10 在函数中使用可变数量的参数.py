#!/usr/bin/python
# Filename:在函数中接收元组或字典.py

#pow()的用法

def sum(p,*args):
    '''
在函数中接收元组或字典时，分别使用*和**前缀。
这种方法在函数需要获取可变数量的参数（参数数量是可变的）时使用
在args变量前有*前缀，所以除了第一个参数外，其余都会作为一个元组存储在args中
'''
    t = 0
    for i in args:
        t = t + pow(i,p)    #pow()用法见下
    print(t)

#pow()里可有两个或三个参数。
#pow(x,y)表示x的y次幂（即x**y）
#pow(x,y,z)表示x的y次幂后除以z的余数（即x**y%z）


sum(2,3,4)  #p=2,args=[3,4],i=3,pow(3,2)=9=t,i=4,pow(4,2)=16,t=9+16=25

sum(2,10)   #p=2,args=[10],i=10,pow(10,2)=10**2=100=t

