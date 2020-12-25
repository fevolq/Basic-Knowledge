#!/usr/bin/python
# Filename：global定义全局变量.py

#global定义的全局变量不是函数定义是的变量

x = 25
def func(a):
    global x                    #global语句用于定义全局变量
                                #即这个函数内的变量x的赋值可以作用于全局主块

    print('x是',x,id(x))     #仍然指向主块中的对象（的内存地址）
    x = 2                   #参数改变，则新生成一个对象
    print('函数块中的x变为了',x,id(x))

print(id(x))
func(99)
print('主块中的x是',x,id(x))     #由于使用global全局定义，所以指向参数改变后的对象



#global可以为定义在函数外的变量赋值，而且同一个global语句可以指定多个全局变量

#注意，使用global定义的全局变量不能是定义函数时的形参，即不能“global a”

#这里的形参a，在函数里的改变能否影响全局，取决于a的类型（可变类型或不可变类型）
