#python3.7
#Filename:装饰器基本功能.py

def a():    #介绍
    """
装饰器就是对被装饰的对象（函数、类）进行重构的，其可以在不改变原来对象的情况下调用对象时执行重构后的行为 
1.解决问题：在函数执行之前和执行之后添加功能，调用函数的方式改变了 
2.不改变原有函数的调用方法:函数里面嵌套函数，并且返回嵌套的函数
    """
    def login():
        print('（初始）快乐')
        print('（初始）login...')
        print('（初始）欢迎下次光临...')
    #login()

    #为避免在大的函数中操作，将欢迎语独立出来，另建函数
    def desc(f):
        def add_info():
            print('快乐')
            f()
            print('欢迎下次光临')
        return add_info     #返回一个函数类型（函数名）
    def login():
        print('login...')

    login = desc(login)  #这个login是新变量，不是原函数
    login()
        
    #desc(login)()  #desc(login)的返回值是一个函数类型，不是调用这个函数，要调用，则需加上括号
    #print(desc(login))
    #print(type(desc(login)))

def b():    #语法糖
    """
在Python中，可以使用”@”语法糖来精简装饰器的代码，把 decorator 置于函数的定义处，
免去给函数重新赋值( 即function = decorator(funtion))
    """
    import time

    def funcA(f):
        start_time = time.time()
        print('开始时间：',start_time)
        print('A')
        a = f()
        end_time = time.time()
        print('结束时间：',end_time)
        return a    #返回值为所要装饰的函数，没有加()，因为不是在调用函数，而是在返回该函数

    @funcA          #调用语法糖，此处相当于funcA(funcB())
    def funcB():
        time.sleep(1)
        print('B')


def b1():   #累积装饰
    """
say()为原函数，需要返回“<b><i>Hello World</i></b>”
    """
    def makebold(f):
        def wrapper(*args,**kwargs):
            res = "<b>" + f(*args,**kwargs) + "</b>"
            return res  #返回值为所要装饰的函数
        return wrapper  #返回值为所要修饰函数所添加的模块，即需要在原函数中添加wrapper函数的内容

    def makeit(f):
        def wrapper(*args,**kwargs):
            res = "<i>" + f(*args,**kwargs) + "</i>"
            return res
        return wrapper

    @makebold   #注意顺序，等同于say=makebold(makeit(say))，但使用这个语法时，原始函数say必须先定义
    @makeit     #从上到下调用装饰器，封装器wrapper的内容也是从上到下执行
    def say(x,y):
        return x+y

    print(say('Hello',' World'))
    #print(say(1,2))    #不同类型不能相加

def c():    #保留函数名和文档信息
    """
使用内置的functools模块中的wraps函数，来保留函数名和文档
    """
    import functools
    import time

    def timeit(func):
        @functools.wraps(func)      #内置装饰器，用来保留原函数名和文档
        def wrapper(*args,**kwargs):
            """这是一个封装器"""
            start_time = time.time()
            res = func(*args,**kwargs)
            end_time = time.time()
            print(start_time,end_time)
            return res
        return wrapper

    @timeit
    def function():
        """原始函数"""
        print('原始')

    function()     #用来执行封装器
    print("函数名：",function.__name__)     #可将装饰器内的语法糖（内置的装饰器）注释掉再执行，查看结果
    print("函数文档：",function.__doc__)
            

if __name__ == '__main__':
    c()
