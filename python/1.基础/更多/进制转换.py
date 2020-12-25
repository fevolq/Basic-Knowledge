#!/usr/bin/python
#Filename:进制转换.py

while True:
    #t = input('请输入一个“整数”或结束：')
    t = 66
    if t == '结束':
        break
    else:
        n = int(t)
        b = bin(n)

        print('\n十进制转换十六：%s——》%#X'%(n,n))
        print('\n十进制转换八：%s——》%#o'%(n,n))
        print('\n十进制转换二：%s——》%s\n'%(n,b))

        break

def turn():     #使用内置函数转换进制
    x = 66
    
    a = bin(x)
    print("转换为二进制：",a)

    b = oct(x)
    print("转换为八进制：",b)

    c = hex(x)
    print("转换为十六进制：",c)

turn()

print("\nDone")
