#!/usr/bin/python3.7
#Filename:返回一个方框.py

def box(symbol,width,height):
    if len(symbol) != 1:
        raise Exception("symbol必须是一个字符")
    if width <= 2:
        raise Exception("宽度必须大于2")
    if height <= 2:
        raise Exception("高度必须大于2")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)

for sym,w,h in (("w",4,4),("0",20,5),("x",1,3),("ZZ",3,3)):
    try:
        box(sym,w,h)
    except Exception as err:
        print("发生了异常：" + str(err))


#box("*",8,5)
