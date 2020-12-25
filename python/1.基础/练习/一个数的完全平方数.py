#!/usr/bin/python3.7
#Filename:求一个数的完全平方数

a = int(input("输入一个正整数："))
n = 0

if a >= 0:
    for i in range(1,a+1):
        if a == i*i:
            print(i)
        else:
            n += 1
    if n == a:
        print("不存在")
        
elif a < 0:
    print("负数不存在完全平方数")

print("\nDone")
