#!/usr/bin/python
#Filename:选取数字组成互不相同无重复的三位数.py

#在1、2、3、4中选取，能组成多少种互不相同且无重复数字的三位数？
#利用三次for循环

sum = 0

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a != b and b != c and c !=a:
                print("%s%s%s"%(a,b,c),end='，')  #将abc输出在一起
                sum = sum + 1

print('\n共有%d种情况'%sum)
