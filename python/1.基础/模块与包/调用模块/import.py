#!/usr/bin/python
# Filename：import.py

#调用的模块与此模块内同名的变量名不冲突（即不是同一个）

import my_test              #调用my_test这个模块

my_test.sayhi()             #使用所调用的模块中的函数
print('v=',my_test.v)        #使用所调用的模块中的变量


#调用模块时，所调用的模块必须处于和本模块同一目录中，
#或放在sys.path所列的目录之一内。

#直接import模块时，会运行所导入的模块的主块
