#!/usr/bin/python3.7
#Filename:斐波那契数列的前n项.py

a = int(input('需要斐波那契数列的前多少项：'))

def fib(n):
    if n<1:
        return None
    elif n==1:
        return [1]
    elif n==2:
        return [1,1]
    else:
        fibs = [1,1]
        for i in range(2,n):
            fibs.append(fibs[i-1]+fibs[i-2])    #当i>2时，fibs列表内已有i个元素，所以此步是取列表内最后两数之和
    return fibs

print(fib(a))
