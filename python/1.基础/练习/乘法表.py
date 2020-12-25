#!/usr/bin/python3.7
#Filename:乘法表.py

#需要注意输出的格式

for i in range(1,10):
    for j in range(1,10):
        print(j,"x",i,"=",i*j,end="   ")  #注意ij的输出顺序
        if i==j:
            print("\n") #用来打断时将输出换行
            break       #当ij相同时，打断j的迭代循环，所以分界线右边不输出

#break打断最近的for/while循环
