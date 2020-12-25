#!/usr/bin/python
# Filename：my_test.py

#解释了__name__这个系统变量

def test():
    print('这是我创建的模块\n')
    '''if __name__ == '__main__':
        print('就是在当前模块，','此时模块的名称是%s\n'%__name__)
    else:
        print('这个模块是从其他处调用的，','模块的名称为 %s\n'%__name__)'''

test()

if __name__ == '__main__':
    print('就是在当前模块，','此时模块的名称是%s\n'%__name__)
else:
    print('这个模块是从其他处调用的，','模块的名称为 %s\n'%__name__)


'''__name__这个系统变量充当了当前模块执行过程中的名称。
如果这个if、else语句就是在本模块中运行，则__name__的名称就是__main__；
如果这个模块被其他模块调用，那么if、else就是在其他模块运行，
则__name__的名称就是当前这个模块所取得名称，且不包含路径，即my_test'''


