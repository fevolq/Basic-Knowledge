#python3.7
#装饰器预览.py

#装饰器是一个函数，其参数为另外一个函数
def decorator(func):

    #在内部定义了另一个函数：一个封装器
    #这个函数将原始函数进行封装，所以可以在原始函数之前或之后执行一些代码
    def wrapper():

        #放一些在原始函数执行之前的一些代码
        print("原始函数执行之前")

        #执行原始函数
        func()

        #放一些在原始函数执行之后的一些代码
        print("原始函数执行之后")

    #此时，“func”函数还没有被执行，所以返回创建的封装函数
    #封装器包含了函数以及其前后执行的代码，已经准备完毕
    return wrapper

#原始函数（永远不会再次接触或更改的函数）
def stand_function():
    print("原始函数，不再更改")

#现在需要把原始函数封装实现功能的扩展，可以将其给装饰器
#装饰器会动态地把 原始函数和需要扩展的功能代码封装，并返回一个新的可用的函数
func_decorated = decorator(stand_function)
func_decorated()

#若要每次调用原始函数（stand_function）时，实际是调用装饰器func_decorated函数，则可用原函数名来给其赋值（即stand_function = decorator(stand_function)）
