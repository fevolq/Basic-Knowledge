#!python3.7
#Filename:内置的排序方法.py

#使用内置的sort()方法和sorted()方法
#sort(*,key=None,reverse=False)——默认时
#sorted(iterable,/,*,key=None,reverse=False)

a1 = [1,2,3,0]
b1 = sorted(a1)     #sorted()方法可用于赋值，但不改变原列表
a1.sort()           #sort()方法无法用于赋值，但改变原列表(即原地更改)
print("b1：",b1)
print("a1：",a1)

print()

a2 = ["123","123456","4567","66"]    #全都是数字，但是字符型
a2.sort(key=int)
print("a2：",a2)

print()

a3 = [("a",2),("d",3),("b",0)]
a3.sort(key=lambda x:x[1])      #x指代列表内的元组，此步表示按照元组内的第二个元素进行排序
print("a3：",a3)
a3.sort(key=lambda x:x[1],reverse=True)     #reverse反转
print("a3：",a3)

print()

#多级排序
import operator
a4 = [(1,2,3),(2,3,4),(0,1,2)]
a4.sort(key=operator.itemgetter(1,2))   #根据元组内第二个和第三个元素进行排序
print("a4：",a4)
