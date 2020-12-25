#!/usr/bin/python
# Filename：调试1.py

import my_test1         #此逻辑行会将所调用的模块全部运行一遍（即运行主块）
                             #由于调用模块内的if不满足，故不运行函数

my_test1.test()
#此逻辑行会直接运行所调用的函数，所得到的结果便是此逻辑行导致的

