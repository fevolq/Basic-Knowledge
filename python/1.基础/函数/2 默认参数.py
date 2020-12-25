#!/usr/bin/python
# Filename：func_默认参数.py

def say(a,b = 1):       #参数b的默认值为1，若用户没有重新定义b，则取1
    print(a * b)
    
say('啊')                
say("m",3)              #重新定义b为3



#只有在形参表的末尾的参数才可以有默认值，默认参数值应该是一个参数
#例：def func(a,b = 1): 有效     而def func(a=1,b): 无效
