#!/usr/bin/python
# Filename：break.py

#用来返回输入的字符长度。

a = True
while a:
    s = input('随便输入什么：')
    if s == '离开':
        break
    print('输入的字符长度为：',len(s))
print('结束')


#break用来终止循环，即便循环条件没有变为False或序列还没有完全递归，
#运行到break都会停止继续循环。
#如果for或while循环被break停止，则对应的esle块不会被执行
