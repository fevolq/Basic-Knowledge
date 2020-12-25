#!/usr/bin/python
# Filename：__init__.py

class person:
    def __init__(self,name):
        self.name = name        #将变量参数name赋值给另一个变量，这个变量就是__init__创建的域
                               
    def yourname(self):
        print('我的名字是',self.name)

p = person('abc')              
p.yourname()                #或person('abc').yourname()


#这里，__init__方法被定义为取了一个参数name（以及普通参数self），self.name是创建的域
#在创建新实例时，我们通过把参数name放在类名的括号内，来传递给__init__方法。
