#!/usr/bin/python
# Filename：continue和break.py

a = True
while a:
    s = input('随便输入什么：')
    if s == '离开':
        break
    elif len(s) < 3:
        print('长度太小')
        continue
    print('有效长度')
print('结束')

