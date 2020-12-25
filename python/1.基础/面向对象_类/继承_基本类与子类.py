#!/usr/bin/python
# Filename：继承_基本类与子类.py

#一个学校内的老师和学生的信息

#父类（基本类、超类）——子类（导出类）

class member:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('\n新增加了%s成员'%self.name)

    def tell(self):
        print('名字是：%s ， 年龄是：%s'%(self.name,self.age),end = ' ， ')


class teacher(member):      #为了使用继承，把基本类的名称作为一个元组放在子类（定义类）的名称后
    def __init__(self,name,age,salary):
        member.__init__(self,name,age)      #调用基类构造的函数
        self.salary = salary
        print('新增加的老师是：%s\n'%self.name)

    def tell(self):
        member.tell(self)       #print("名字是：{}，年龄是：{}，工资是：{}".format(self.name,self.age,self.salary))
        print('工资是：%s'%self.salary)     #可以在子类中覆盖基本类的方法

class student(member):
    def __init__(self,name,age,marks):
        member.__init__(self,name,age)
        self.marks = marks
        print('新增加的学生是：%s\n'%self.name)

    def tell(self):
        #member.tell(self)
        print('成绩是：%s'%self.marks)


t = teacher('a','b','c')          #此时使用时，不再需要输入额外的参数self。使用没有注明的英文字符时，要引号
s = student(1,2,3)

ms = [t,s]             #将用户要使用的对象放入一个元组或列表

for mem in ms:         #调用了子类型中的tell函数（方法），而不是基本类型的tell
                            #python总是首先查找对应类型的方法。如果不能在子类中找到对应的方法，才开始到基本类中逐个查找
    mem.tell()
'''
teacher('a','b','c').tell()
'''
print('\nDone')

#注意程序运行的顺序。先运行t（运行teacher类中的__init__），再运行s（运行__init__），最后依次运行for内的指定类中的tell函数（注意是否为子类，且是否包含应用了父类中的函数）。

#在多重继承时，注意继承的顺序
    
