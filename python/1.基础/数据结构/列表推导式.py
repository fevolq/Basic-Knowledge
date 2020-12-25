#!/usr/bin/python3.7
#Filename:列表推导式.py

#列表的推导式（集合、字典也支持推导），没有逗号冒号

list1 = [1,2,3,4]

a = [i for i in list1]
print(a,"\n")

b = [i*5 for i in list1]
print(b,"\n")

c = [[i,i**2] for i  in list1]
print(c,"\n")

d = [i for i in list1 if i > 2]
print(d,"\n")

list2 = [6,7,8,9]

e = [x*y for x in list1 for y in list2]
print(e,"\n")

f = [list1[i]*list2[i] for i in range(len(list1))]
print(f,"\n")

print("")

#嵌套列表，3x4转换为4x3
list3 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ]

g = [[x[i] for x in list3] for i in range(4)]
print(g,"\n")

h = []
for i in range(4):
    h.append([x[i] for x in list3])

print(h,"\n")

m = []
for i in range(4):
    m_1 = []
    for n in list3:
        m_1.append(n[i])
    m.append(m_1)

print(m,"\n")

