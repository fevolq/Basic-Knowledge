#python3.7
#Filename:yield的解析.py

#有yield的函数是一个生成器函数，使用for...in...或next()来反映出值


def fab1():
    def fab(max):
        """斐波那契数列前多少项"""
        n,a,b = 0,0,1
        while n<max:
            print(b)
            a,b = b,a+b
            n += 1
    fab(5)
    """函数返回为None，所以复用性较差。"""

def fab2():
    def fab(max):
        n,a,b = 0,0,1
        l = []
        while n<max:
            l.append(b)
            a,b = b,a+b
            n += 1
        return l

    for n in fab(5):
        print(n)
    """可复用，但随着max增大，占用的内存也增大，所以最好不要用list来保存中间结果。"""

def fab3():
    """改写为一个迭代对象"""
    class Fab():
        def __init__(self,max):
            self.max = max
            self.n,self.a,self.b = 0,0,1

        def __iter__(self):
            return self

        def next(self):
            if self.n < self.max:
                r = self.b
                self.a,self.b = self.b,self.a+self.b
                self.n = self.n+1
                return r
            raise StopIteration()

    for n in Fab(5):
        print(n)
"""Fab类通过next()不断返回数列的下一个数，内存占用始终为常数。
但代码不够简洁。"""

def fab4():
    """使用yield"""
    def fab(max):
        n,a,b = 0,0,1
        while n<max:
            yield b
            a,b = b,a+b
            n += 1

    print(fab(5))
    for n in fab(5):
        print(n)
"""在保持了简洁性的同时，也获得了迭代的效果。"""

if __name__ == "__main__":
    fab4()
    

"""
yield 的作用就是把一个函数变成一个生成器，
带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个生成器。
调用fab(5)不会执行fab函数，而是返回一个迭代对象。

在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，
执行到 yield b 时，fab 函数就返回一个迭代值，
下次迭代时，代码从 yield b 的下一条语句继续执行，
而函数的本地变量看起来和上次中断执行前是完全一样的，
于是函数继续执行，直到再次遇到 yield。
在for循环中会自动调用next()方法。

也可手动调用fab(5)的next()方法。
如：（调用fab函数）
>>>f = fab(5)  >>>f.next()   1    >>>f.next()   2
"""

def fab(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n += 1

from inspect import isgeneratorfunction

isgeneratorfunction(fab)    #返回True
#fab是一个生成器函数，而fab(5)是调用fab返回的一个生成器，好比类的定义和类的实例的区别。

#每次调用fab函数都会生成一个新的生成器，相互之间不影响。
#在一个生成器函数中，如果没有return，则默认执行至函数完毕，如果在执行过程中遇到return，则直接终止迭代。






    


    
