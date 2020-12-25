#python3.7
#Filename:异常信息、抛出异常、传递异常.py

#获取异常信息
def a():
    try:
        a = 2/'1'
    except Exception as e:
        print(e)

#抛出异常
def b():
    """
发生异常时，执行了except语句，还通过raise再次抛出了异常。
捕捉到了异常，但是又想重新引发它，使用不带参数的raise语句即可。
    """
    try:
        a = 2/0
    except:
        print("错误")
        raise               #直接重新抛出异常
        #raise Exception('error')    #重新抛出异常，且自定义了异常的信息
#主动抛出异常，try用法和自定义异常类似，不过用的是内置的异常类型

#传递异常
def c():
    """
异常的传递—— 当函数/方法执行出现异常，会将异常传递给 函数/方法 的调用一方，
如果传递到主程序，仍然没有异常处理，程序才会被终止。
    """
    #eg1：demo1()发生异常，传递给demo2()，再传递给主程序print()函数
    def demo1():
        return int(input("输入整数："))
    def demo2():
        return demo1()
    try:
        print(demo2())
    except ValueError:
        print("错误，请输入整数")
    except Exception as e:
        print("未知错误 %s"%e)

    print('\n\n')
    #eg2：try的嵌套传递异常
    
    #open就异常，所以后面的不会执行，直接判断except语句的异常类型
    try:
        f = open('1.txt','r')
        try:
            print(a)
        except FileExistsError as e:
            print("文件存在报错",e)
    except NameError as e:
        print("名字错误",e)
    except BaseException as e:
        print("程序内部异常",e)

    #open没问题，往下执行，print(a)引发异常，但与内部的try指定的异常类型不符，所以这个异常会传递到外层的try，
        #若外层的try有这个异常类型的处理，则执行外层的except，否则继续往外，知道传递到主程序，有python解释器来把程序终止。
    try:
        f = open('del.txt','w')
        try:
            ab = ab+1
        except FileNotFoundError as e:
            print("没有找到文件",e)
    except NameError as e:
        print("名称异常",e)
    except TypeError as e:
        print("类型异常",e)
    except:
        print("error")
        raise

if __name__ == '__main__':
    pass
