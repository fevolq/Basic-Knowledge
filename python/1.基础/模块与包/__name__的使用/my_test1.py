#!/usr/bin/python
# Filename：my_test1.py

#避免调用模块时，重复运行了模块内的函数。

def test():
    print('模块的名称是%s'%__name__)
    print('1')
if __name__ == '__main__':
    test()
else:
    pass
        
'''
这个模式能在调用这个模块的时候，避免执行两次函数的操作。
还可以在本模块中直接运行这个函数
'''
