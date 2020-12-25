#!/usr/bin/python
# Filename：变量参考与拷贝列表.py

a = ['1','2','3','4','5']
b = a                           #这一步只是将a列表赋给变量b,但是b并不新生成一个列表
                                #a与b共用一个列表（指向同一个内存地址）
print('a是',a,id(a)),print('b是',b,id(b))

del a[0]
print('\na是',a),print('b是',b)
del b[0]
print('a是',a),print('b是',b)     #a与b共一个列表，所以一旦改动，ab都会变

c = a[:]    #c = a.copy()         #此处是将a列表拷贝一份给c，所以会新生成个c列表
print('\na是',a,id(a)),print('c是',c,id(c))

del a[0]
print('\na是',a),print('b是',b),print('c是',c)
del c[-1]
print('a是',a),print('b是',b),print('c是',c)   #ab联动，c单独


#给创建的对象a赋予了一个变量b，b仅仅参考对象a列表，就是指向内存中的a列表
#赋值语句不创建拷贝
#想要复制一个列表或类似的序列或其他复杂的对象，必须用切片操作来建立拷贝

#深拷贝与浅拷贝
