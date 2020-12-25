#python3.7
#Filename:装包与解包.py

#装包
def package():  
    def f1(n,*args):    #接收可变（数量）参数
        """
形参中的*args是接受数据的args，它是一个元组，把传入的数据放进args元组中。
函数中的args仍然是元组， *args就是将元组的数据进行拆包，一开始输入的形式
        """
        print(n)
        print(args)     #未拆包
        print(*args)    #进行拆包
    f1(1,2,3,4)

    def f2(**kwargs):
        """
*args用来接受多余的未命名参数， **kwargs是用来接受命名参数。函数中args是元组，kwargs是字典
装包的意义就是把未命名的参数和命名的参数放在元组或字典中。
        """
        print(kwargs)   #未拆包
        print(*kwargs)  #进行拆包,只有key
        #print(**kwargs)    #异常，除非{**kwargs}。参见qs.f()
    f2(a=1,b=2)

#解包
def unpackage():
    """
1. 解包的意义就是将传递给函数的一个列表，元组，字典，拆分成独立的多个元素然后赋值给函数中的参变量。
2. 解压字典有两种解发，一种用*解的只有key，一种用**解的有key，value。但是这个方法**只能在函数定义中使用。
    """
    def f(*args,**kwargs):
        for arg in args:
            print(arg)
        for key,value in kwargs.items():
            print(key,value)
    f(1,2,3,a=4,b=5,c=6)    #123都赋值给args，关键字参数都给kwargs





#一些应用问题
class qs(object):
    #在传入参数时，可变参数(*)之前不能指定参数名来传参
    def a(n,*args):
        print(n)
        print(args)
    def _a():
        qs.a(1,2,3,4)
        #qs.a(n=1,2,3,4)   #会导致异常

    #在传入参数时，可变参数(*)之后的参数必须指定参数名来传参，否则会被归到可变参数中
    def b(n,*args,m=None):
        print(n)
        print(args)
        print(m)
    def _b():
        qs.b(1,2,3,m=4)

    #关键字参数都只能作为最后一个参数，前面的参数按照位置赋值或是名称赋值都可
    def c(n,*args,m,**kwargs):
        print(n)
        print(args)
        print(m)
        print(kwargs)
    def _c():
        qs.c(1,2,a=7,m=3,b=8,c=9)
    def c1(n,m,*args,**kwargs):
        print(n)
        print(args)
        print(m)
        print(kwargs)
    def _c1():
        #qs.c1(1,2,3,a=7,b=8,m=6)   #异常
        qs.c1(1,6,2,3,a=7,b=8)

    #使用函数时，在传入参数时的解包
    def d(a,b,c):
        print(a,b,c)
    def _d():
        l = [1,2,3]
        qs.d(*l)    #可传入三个参数，或传入一个包含3个元素的可迭代对象，用*进行解包
    def _d_():
        d = {'a':1,'b':2,'c':3}
        qs.d(*d)    #一个*号传入的实参为key值
        qs.d(**d)   #两个**号传入的实参为value值

    #python中的自动解包
    def f():
        a,b,c = [1,2,3]
        print(a,b,c)
        a,b,c = {'A':1,'B':2,'C':3}
        d = {'A':1,'B':2,'C':3}
        print(a,b,c)    #解包只会把字典中的key值取出，value则去掉了
        print(*d)
        a,b,*c = [1,2,3,4]
        print(a,b,c)

        print(*range(4),4)          #0 1 2 3 4
        print([*range(4),4])        #[0, 1, 2, 3, 4]
        print({'x':1,**{'y':2}})    #{'x': 1, 'y': 2}

        #合并两个字典（且不更改原字典）
        x = {'a':1,'b':2}
        y = {'m':3,'n':4}
        print({**x,**y})

if __name__ == '__main__':
    qs.f()














