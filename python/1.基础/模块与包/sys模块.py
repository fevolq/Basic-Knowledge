#!/usr/bin/python
# Filename：sys.py

#sys模块是系统模块

import sys

print('这个文件的路径是：',sys.argv)     #以列表形式返回文件的绝对路径

for i in sys.argv:
    print(i)


print('\n\n这个文件的环境变量是：',sys.path,'\n')

    
