#!/usr/bin/python
# Filename：类_使用对象的方法.py

class person:
    def sayhi(self):        #注意self，类方法必须包含一个参数，它代表类的实例
        print('hello')

person().sayhi()            #与下面相同

p = person()                #使用类时，（若没有变量）不要忘记类名后加上括号
p.sayhi()
print(p)        #与下面的类进行对比

person()    #由于此类内没有__init__，且类内的输出位于一个函数内，所以这个实例化没有返回值

#使用类时，一定要先实例化(即person())

#当类是父类，即没有继承其他类时，默认是继承object类。即可写成class person或class person(object)
#当类是子类时，类名后一定要跟着一个括号，包含所继承的类名

print('\n')
class test:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "该对象的name是{}，age是{}".format(self.name,self.age)

    def run(self):
        print("name：{}；age：{}".format(self.name,self.age))

t = test('a',18)    #实例化
t.run()
print(t)
#当类中定义了__str__方法时，直接打印对象的名称，会直接调用这个方法，且返回的是方法中的return语句
