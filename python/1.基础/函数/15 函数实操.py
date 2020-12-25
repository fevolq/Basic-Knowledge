#!/usr/bin/python
# Filename：函数实操.py

def printMax(a,b):
    c = 0
    if a > b:
        return '%s较大'%a
    elif a == b:
        return '一样大'
    else:
        return '{}较大'.format(b)
while True:
    s = input('输入开始或结束：')
    if s == '结束':
        break
    elif s == '开始':
        a = input('输入一个数a= ')
        b = input('再输入一个数b= ')
        print(printMax(a,b))
    else:
        continue
print('over')

"""
print(printMax.__code__)        #返回这个函数所在文件的路径以及函数在文件内的行数
print(printMax.__code__.co_varnames)    #返回这个函数内定义的所有变量（包括且不限于函数的参数）
print(printMax.__code__.co_filename)    #返回这个函数所在文件的路径

可用于寻找导入模块内的函数
"""
#print(printMax.__code__.co_filename)
#print(printMax.__code__.co_varnames)
#print(printMax.__code__)
