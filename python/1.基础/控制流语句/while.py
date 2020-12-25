#!/usr/bin/python
# Filename: while.py

n = 23
r = True
while r:
    g = int(input('输入一个数'))
    if g == n:
        print('猜对了')
        r = False     #将False赋值给r，从而使while语句不再继续循环
    elif g < n:
        print('那个数大一些')   #此时，r仍是True，所以继续重新执行while循环
    else:
        print('那个数小一些')   
else:
    print('while循环结束')

print('完成')


#while语句是循环语句。在条件为真的情况下，while语句会重复执行所包含的语句，
#只有在条件是False时才会停止循环。
#while语句可以有一个可选的else，当while的循环条件变为False时，else块才被执行
#如果while循环有一个else，它将始终被执行，除非while永远循环下去。
