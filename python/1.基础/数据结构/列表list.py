#!/usr/bin/python
# Filename：列表list.py

list = ['苹果','香蕉','水杯','牙膏','伞']
print('我有',len(list),'样东西要买。'), #len(list)判断列表内有多少个字符串
print('它们分别是：')
for i in list:                      #迭代
    print(i,end = ' ')

print('\n我还需要被子'),
list.append('被子')               #在列表里添加一个字符串（格式：列表名.append('an item')）
print('现在我需要买：',list),

print('现在我要对清单进行排序')
list.sort()                     #对列表排序
print('排序后的清单是：',list)

print('我首先要买',list[0])
old = list[0]
del list[0]                 #删除列表内的第一个对象
print('我已经买了',old)    #由于上一步已经删除了列表内的第一个对象，所以需要在删除前，先把它赋值给一个变量
print('我还需要买',list)


#len()判断字符串长度
#列表名.append('an item')  添加列表内的项目
#使用列表的sort方法来对列表排序，影响列表本身
#del语句，删除某个对象或列表本身
#在print语句后增加一个逗号和end语句组合来消除每个print语句自动打印的换行符
