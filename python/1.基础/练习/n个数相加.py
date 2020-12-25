#!/usr/bin/python
#Filename:n个数相加.py

print("结束请输入“over”\n")
sum = 0
n = 0
while True:
    a =  input("请输入：")
    if a == "over":
        break
    else:
        b = int(a)
        sum = sum + b
        n = n + 1

print("\n共%d个数相加，和是：%d"%(n,sum))
