#!/usrbin/python3.7
#Filebname:类的私有.py

#类内私有的变量或方法(函数)在类内自己调用

#类的私有变量（属性）
class counter1:
    public_a = 0   #公开变量
    __secret_a = 0  #私有变量（指类内私有）
    def __init__(self):
        pass

    def count(self):
        self.public_a += 1
        self.__secret_a += 1
        print(self.__secret_a)

counter = counter1()    #实例化
counter.count()
counter.count()
print(counter.public_a)
#print(counter.__secret_a)      #报错，实例不能访问私有变量
#若想要在外部访问或修改类内私有属性，可在类内添加一个访问私有属性的方法，通过访问方法来达到目的
#print(counter._counter1__secret)   #此种方法也可以访问私有属性，但不建议这么做。可能会修改类中的属性名字

print("\n")

#类的私有方法（函数）
class site:
    def __init__(self,name,age):
        self.name = name        
        self.age = age          

    def who(self):
        print("名字是：{}".format(self.name))
        print("年龄是：{}".format(self.age))

    def __foo(self):        #私有方法（名称前有两个下划线）
        print("私有方法")

    def foo(self):          #公共方法
        print("公共方法")
        self.__foo()        #在类内调用一次私有方法

s = site("呵呵",666)
s.who()
s.foo()
#s.__foo()          #报错。这一步在类外，不能调用类的私有方法

