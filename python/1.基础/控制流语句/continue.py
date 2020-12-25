#!/usr/bin/python
# Filename：continue.py

#判断输入的字符长度是否大于等于3，返回“有效长度”。

a = True
while a:
    s = input('随便输入什么：')
    if s == '离开':
        break
    elif len(s) < 3:
        continue
    print('有效长度')
print('结束')

#continue用来跳过当前循环的内的剩余语句，再重新进行下一轮的循环。也可用于for循环
#len()函数用来取得括号内的字符长度

