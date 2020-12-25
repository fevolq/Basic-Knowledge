#!/usr/bin/python
# Filename:lambda在运行函数时创建新的函数.py

def make(n):
    return lambda s: s*n
'''
lambda需要一个参数，后面仅跟单个表达式作为函数体，
表达式的值被这个新建的函数返回。
'''
t = make(2)
print(t('word'))
print(t(5),'\n')

t = make(4)
print(t('word'))
print(t(6),'\n')

#lambda语句被用来创建新的匿名函数对象
