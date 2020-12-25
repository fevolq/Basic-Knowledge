#!/usr/bin/python
# Filename：调试.py

import my_test

my_test.test()      #若此行被注释掉，则不会再执行一遍所调用模块的这个函数

#注意调用模块内函数的方法（或from my_test import test，则只调用模块内的函数，不会运行主块）    


#由于调用的模块中的主块已经调用了函数，所以在此调用模块时会运行那个主块。
