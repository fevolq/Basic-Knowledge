#python3.7
#Filename:属性.py

#注：不能在外面直接更改类中的私有属性，因为在外面无法访问类内私有属性。但是可以通过在类内创建函数方法，来访问和修改私有属性

class test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def save(self):
        print(self.a,self.b)

t1 = test(1,2)  #实例化，创建一个对象
t1.save()
print('\n')

#修改对象的属性值
print(t1.a,t1.b)
t1.a = 6            #常规修改。对象.属性名 = 属性值
print(t1.a)
t1.c = 3            #如果这个属性在对象中不存在，则会添加这个属性
print(t1.c)
setattr(t1,'b',9)   #setattr(o,name,value)。o：设置属性的对象；name：要设置对象的属性名；value：要设置的属性值
print(t1.b)

#删除对象的属性(删除后就不能再使用了)
del t1.a            #常规删除
#print(t1.a)
delattr(t1,'b')     #delattr(o,name)。o：要删除的对象；name：要删除的属性名
#print(t1.b)

#判断对象是否拥有某个属性
s1 = hasattr(t1,'a')    #判断会返回结果。有这个属性就返回True，没有就返回False
s2 = hasattr(t1,'c')
print(s1,s2)


print('\n')
#限制实例的属性
class student:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        __slots__ = ('name','age')

s = student(1,2)       #实例化
s.name = "abc"
s.age = 18
print(s.a,s.b,s.name,s.age)
#s.sex = 'fale'     #异常
#通过__slots__用元组来限制实例可以添加的属性
#注：__slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用。但是在子类中定义__slots__，则子类实例允许定义的属性就是自身的加上父类的__slots__。
