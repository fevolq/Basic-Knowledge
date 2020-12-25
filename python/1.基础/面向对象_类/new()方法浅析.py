#python3.7
#Filename:new()方法浅析.py

"""
使用类名()创建对象时，python的解释器首先会调用new方法为对象分配空间 
_ new _是一个由object基类提供的内置的静态方法，主要有两个作用： 
    在内存中为对象分配空间 
    返回对象的引用 
python的解释器获得对象的引用后，将引用作为第一个参数，传递给_ init _方法。 
_ new _：负责给对象分配空间 _ init _(初始化方法)负责给对象初始化

"""
class a(object):
    def __init__(self):
        print('a.init')

    def __new__(cls,*args,**kwargs):
        print('a.new')
        return object.__new__(cls,*args,**kwargs)
        #return a.__new__(cls,*args,**kwargs)   #调用自身的new()来制造实例是，会造成死循环

class b(a):
    def __init__(self):
        print('b.init')

    def __new__(cls,*args,**kwargs):
        print('b.new')
        return a.__new__(cls,*args,**kwargs)

class c(a):
    def __init__(self):
        print('c.init')

class d(a):
    def __init__(self):
        print('d.init')

    def __new__(cls,*args,**kwargs):
        print('d.new')
        return object.__new__(cls,*args,**kwargs)

#a = a()

b = b()

#c = c()     #类中没有定义new()方法时，会自动调用其父类的new()方法来制造实例

d = d()

"""
1.new()是在新式类中新出现的方法，它作用在构造方法init()建造实例之前
2.在Python 中存在于类里面的构造方法init()负责将类的实例化，而在init()调用之前，new()决定是否要使用该init()方法，因为new()可以调用其他类的构造方法或者直接返回别的对象来作为本类 的实例。
3.如果要得到当前类的实例，应当在当前类中的new()方法语句中调用当前类的父类 的new()方法。

4.如果（新式）类中没有重写new()方法，即在定义新式类时没有重新定义new()时 ，
Python默认是调用该类的直接父类的new()方法来构造该类的实例，
如果该类的父类也没有重写 new()，那么将一直按此规矩追溯至object的new()方法，
因为object是所有新式类的基类。

"""
