#!/usr/bin/python
#Filename:数字排序.py

#3个数的排序

a = []
for i in range(3):
    x = int(input('请输入整数：'))
    a.append(x)
    
a.sort()
print('\n从小到大为%d，%d，%d'%(a[0],a[1],a[2]))
