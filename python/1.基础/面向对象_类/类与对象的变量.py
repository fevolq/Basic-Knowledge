#!/usr/bin/python
# Filename：类与对象的变量.py

class person:
    popu = 0                #类的变量（属性），由所有对象实例共享，当任一对象对其作了改动，这个改动会反映到所有实例上。（a、b对象共享）

    def __init__(self,name):        #构造函数，在生成对象时调用（给类传入变量）
        self.name = name            #类的变量可在类中的所有对象中使用(self.name)，而对象的变量，由自己单独拥有，与其他对象互不相关
        print('\n加入了',self.name)
        person.popu = person.popu + 1

    def __del__(self):              #析构函数，释放对象时调用（这个方法的名称不是私有的表示）
        print('\n%s走了'%self.name)

        person.popu = person.popu - 1

        if person.popu == 0:
            print('%s是最后一个'%self.name)
        else:
            print('还有%s个人在'%person.popu)

    def sayhi(self):
        print('\nhi 我是%s'%self.name)

    def howmany(self):
        if person.popu == 1:
            print('我是唯一一个')
        else:
            print('我们有%s人在'%person.popu)

a = person('a')
a.sayhi()
a.howmany()

b = person('b')
b.sayhi()
b.howmany()

b.__del__()
#del b          #或使用此方法。会自动调用对象的__del__方法。而这个方法一旦被调用，则对象“死亡”，无法再访问。
a.__del__()
#del a
