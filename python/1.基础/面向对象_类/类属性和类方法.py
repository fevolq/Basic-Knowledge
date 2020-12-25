#类属性和类方法
"""
一切皆对象。类也是一个特殊的对象——类对象。拥有自己的属性和方法。
类属性：类属性就是给类对象定义的属性，通常用来记录与这个类相关的特征，类属性不会用于记录具体对象的特征，使用赋值语句在class关键字下方可以定义类属性 。
类方法：类方法就是针对类对象定义的方法，在类方法内部就可以直接访问类属性或调用类方法。。
类有两种属性：静态属性和动态属性

静态属性就是直接在类中定义的变量
动态属性就是定义在类中的方法
"""
class Student:
    #使用赋值语句定义类属性，记录总人数
    popu = 0        #当任一对象对其进行了更改时，会反映到所有实例上
    def __init__(self,name):
        self.name = name
        Student.popu += 1

    @classmethod    #类方法定义使用装饰器
    def popu_count(cls):    #形参写cls，表示传入的是class的引用
        #在类方法内部，可以直接访问类属性或调用类方法
        print("总人数是：",Student.popu)

    
    @staticmethod
    #静态方法
    def a():
        print('abc')

#创建对象
s1 = Student('a')
s2 = Student('b')
s3 = Student('c')   #每次实例化，都会调用__init__方法，所以popu会每次增加

#使用 类名.类属性名 或 对象名.类属性名 来获取类属性
print(Student.popu)
print(s1.popu)

#调用类方法
Student.popu_count()
s1.popu_count()

print('\n')
"""
在开发的时候，如果需要在类中封装一个方法，这个方法 
既不需要访问实例属性或者调用实例方法 
也不需要访问那类属性或者调用类方法 
这个时候可以把这个方法封装成一个静态方法
"""
class A:
    def qwe():
        print('qwe')
        
    @staticmethod
    def abc():
        print('abc')

a = A()
        
a.abc()     #或直接在类内调用(或自运行)静态方法
A.abc()
#a.qwe()    #异常，无法通过对象调用
A.qwe()
