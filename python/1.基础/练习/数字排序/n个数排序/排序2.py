#!/usr/bin/python
# Filename：执行模块.py

import A_modul

a = A_modul.a
print('\n一共有%s个数'%len(a))

for x in range(0,len(a)-1):
    for y in range(1 + x,len(a)):
        if a[x] < a[y]:
            q = int(a[y])       #a[x],a[y] = a[y],a[x]
            a[y] = a[x]
            a[x] = q

print('\n从大到小是 %s'%a)

a.reverse()     #反向序列
print('\n由小到大是',a)

print('\nDone')
