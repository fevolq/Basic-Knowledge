#!/usr/bin/python3.7
#Filename:循环报数.py

#30个人循环报数1到9，数到9的出局。

people = {}
for i in range(1,31):
    people[i] = 1           #30个人依次排列，每个人的值（不是编号）都为1。字典内{编号:1}

le = 0      #离开的人数
a = 1       #30个人的依次编号（1~30）
n = 1       #依次报的数字

#进行循环报数，数到9的编为0（即value为0）
while a <= 31:
    if le == 15:
        break
    elif a == 31:       #循环报数
        a = 1
    else:
        if people[a] == 0:      #跳过已经报数过9的人（值为0）
            a = a+1
        elif n == 9:
            people[a] = 0       #数到9的人的值变为0
            le = le+1
            a = a+1
            n = 1
        else:           #while循环内会首先运行此步
            a = a+1
            n = n+1

#找出字典内值为0的键（编号）组成一个列表
list = []
for i in range(1,31):
    if people[i] == 0:
        list.append(i)
print("第{}号离开".format(list))
