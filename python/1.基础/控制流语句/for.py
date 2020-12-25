#!/usr/bin/python
# Filename：for.py
for i in range(0,5):
    print(i,end=' ')
else:
    print('结束')


#for..in是另一类循环语句，它在一序列的对象上，逐一的使用队列中的每个项目
#else是可选的，如果有，则总是在for循环结束后执行一次，除非for循环内有break打断

#range返回一个序列的数，但是并不真正生成一个序列。range(1,5)表示[1,2,3,4],
#range内只有一个数时，表示从0开始，到这个数的前一个数。有两个数时，第二个数一定要大于第一个数（否则不会有返回结果）
#range(1,10,3)表示[1,4,7]，3用来表示步长，如果range内部只有两个数，则默认步长为1
#range从第一个数开始，但截止处不包含第二个数

print("")
for i in reversed(range(1,10,2)):       #调用reversed()函数反向遍历一个序列
    print(i,end=" ")

for i in range(9,2):    #没有返回结果
    print(i)
