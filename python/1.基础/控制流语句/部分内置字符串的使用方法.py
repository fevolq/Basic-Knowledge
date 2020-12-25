#!/usr/bin/python
# Filename：部分内置字符串的方法.py

a = 'qwerty'

if a.startswith('qw'):
    print('是的，这个字符串以qw开始')

if 't' in a:
    print('\n是的，这个字符串包含t')
else:
    print('\n不，这个字符串不包含t')

if 'a' in a:
    print('是的，这个字符串包含a')
else:
    print('不，这个字符串不包含a')

if a.find('ert') != -1:     #-1表示不在其中
    print('\n是的，它包含ert\n')


b = ['1','2','3']
delimiter = '_*_'
print(delimiter.join(b))
print("-".join(b))


#startswith用来测试字符串的开始字符串
#in操作符用来检验一个给定的字符串是否在另一个字符串中
#find用来找出给定字符串在另一个字符串中的位置
#join可用来返回生成一个大的字符串

#find()方法检测字符串中是否包含子字符串str，
    #检查是否包含在指定范围内，如果包含子字符串则返回开始的索引值，否则返回-1。
