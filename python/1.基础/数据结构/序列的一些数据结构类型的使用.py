#!/usr/bin/python
# Filename：列表的一些数据结构类型的使用.py

a = [66.25,333,1,333,1234]
print(a.count(333),a.count(1234),a.count('a'))   #count(x)返回x在链表中出现的次数
#2 1 0

a.insert(2,-1)              #insert(i,x)在指定位置插入一个元素x，
print(a)                    #a.insert(len(a),x)相当于a.append(x)
#[66.25, 333, -1, 1, 333, 1234]

print(a.index(333))         #index(x)返回列表中第一个值为x的元素的索引
#1

a.append(333)               #append(x)把一个元素x添加到列表的结尾
print(a)                    #相当于a[len(a):] = [x]————x要放在括号内
#[66.25, 333, -1, 1, 333, 1234, 333]

a.remove(333)               #remove(x)删除列表中值为x的第一个元素
print(a)
#[66.25, -1, 1, 333, 1234, 333]

a.reverse()                 #reverse()将链表内的元素进行倒排
print(a)        #直接在列表内更改，不新建，它的返回值是None，所以不能将其赋值给列表
b = a[::-1]     #倒排，且另创建一个列表
#[333, 1234, 333, 1, -1, 66.25]

a.sort()                    #sort()将链表内的元素进行小到大排序
print(a)
#[-1, 1, 66.25, 333, 333, 1234]

a.pop(2)                    #pop(i)从链表的指定位置删除元素，并将其返回
print(a.pop(2))                     #这里已经进行了两步删除操作
#333
print(a)
#[-1, 1, 333, 1234]

a.pop()                     #若是没有指定索引，则删除（返回）最后一个元素
print(a)
#[-1, 1, 333]
