#!/usr/bin/python3.7
# Filename:if判断True和False.py

#if判断True和False

if None:            
    print(1)
else:
    print(2)

if False:
    print("False")
else:
    print("True")

if 0:
    print(3)
else:
    print(4)

if not 1:       #1会转换为布尔型的True。
    print(5)
else:
    print(6)


#当对象为None、False、空字符串""、0、空字典{}、空元组（）、空列表[]时，
#    均会被转换为False，除此之外的其他对象都会被转化成True。

#当对象是False时，if下面的语句块永远不会被执行。
