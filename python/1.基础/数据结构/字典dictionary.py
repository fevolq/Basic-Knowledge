#!/usr/bin/python
# Filename：dict字典.py

ab = {'1':'abc','2':'def','3':'hij',"a":6}
print('1对应%s\n'%ab['1']),
#print('1对应',ab['1'])

ab['4'] = 'xyz'             #在字典内增加键值对，通过索引操作符来寻址一个键并为其赋值
del ab['2']                 #在字典内删除某个键值对

print('ab字典内现在有%s对\n'%len(ab))      #字典内的一个键值对属于一个长度

for m,e in ab.items():      #items()方法可以同时解读键和值
    print('%s对应%s'%(m,e))    

if '4' in ab:
    print('\n4对应%s'%ab['4'])
    
a = {'1':'2'}
b = {'3':'4'}
a.update(b)     #将两个字典合并

#创建空字典
c = {}
d = dict()
print(type(c),type(d))

e = dict('q'='w','a'='s',2='r')     #使用dict关键字创建字典
#print(e)
    
#键值对在字典中的标记方式：d = {键 : 值，键1 ：值1， 键2 ： 值2}
#字典中的键值对没有顺序
'''字典中的items的使用,字典的items用法，会返回一个由元组构成的列表，
    每个元组都包含一对项目——建与对应的值'''
#使用字典内的键值对时，引号不能忘
#键是唯一的
