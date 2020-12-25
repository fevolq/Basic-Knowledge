#python3.7
#Filename:类中的一些特殊的方法.py

class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        pass

    def run(self):
        print("a：{}；b：{}".format(self.a,self.b))
    #以上是一个基本的类

    def __str__(self):
        return "对象中的a是{}，b是{}".format(self.a,self.b)

    def __del__(self):
        print("该对象运行全部结束。")
        pass

t = test('a','b')   #建造一个对象
t.run()

print(t)
#直接打印对象名，会调用类中的__str__方法，返回的是方法中的return语句指定的内容
    #若没有__str__方法，则会返回对象在内存地址中的指向

del t
#del会调用类中的__del__方法，且结束该对象。
    #但是仅在该对象的引用全部被内存删除后才会调用，如果t对象还在其他地方被引用，则不会删除这个对象，__del__也不会触发
print("\n")


class Test:
    T = 0
    def __init__(self,a):
        self.a = a
    def run(self):
        pass

Tt = Test('a')
print(Test.__name__,type(test.__name__))    #查看类的名字
print(Test.__dict__,Tt.__dict__)    #查出的是一个字典，key是属性名，value是属性值
print(Test.__doc__)     #显示注释
print(dir(Test))        #以列表形式返回类的方法（包括属性）
print(Test.__module__)  #类定义所在的模块
print(Test.__class__)
print(isinstance(Tt,Test))  #判断对象是否是类的实例


print('\n')
class basic():
    def __init__(self):
        pass
    def p(self):
        print("basic")

class A(basic):
    def p(self):
        print("a")
class B(basic):
    def p(self):
        print("b")
class C(A,B):
    def p(self):
        print("c")
c = C()
c.p()       #在多继承中，调用某个方法时，会先在本身的类中查找，没有则往上查找父类

print(C.__mro__)    #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.basic'>, <class 'object'>)
#使用类名.__mro__（或类名.mro()）会返回查找这个类中的方法(不论在这个类中是否存在)的先后路径顺序（按C->A->B->basic->object的顺序进行查找方法）
print(C.__base__,C.__bases__)
##__base __只查看从左到右继承的第一个子类，__bases__则是查看所有继承的父类
