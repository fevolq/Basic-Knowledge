#!/usr/bin/python
# Filename：排序1.py

'''a = input('输入一个数a=')
b = input('输入一个数b=')
c = input('输入一个数c=')
d = input('输入一个数d=')
e = input('输入一个数e=')

x  = [a,b,c,d,e]
'''
import A_modul

a = A_modul.a

a.sort()        #自动排序
print('\n一共有%s个数'%len(a))
print('\n由低到高是',a)

a.reverse()     #反向排序
print('\n由大到小是',a)

print('\nDone')

