#python3.7
#Filename:自定义异常.py

#自定义异常，只需自定义异常类继承父类Exception（或者任何一个已经存在的异常类型）。
#在自定义异常类中，重写父类init方法。

#raise()：用raise语句来引发一个异常。异常/错误对象必须有一个名字，且它们应是Error或Exception类的子类。

class ownException(Exception):
    def __init__(self,a):
        super().__init__(a)   #初始化父类
        self.a = a
        #self.b = b

    def __str__(self):
        return self.a
    
try:
    pass
    raise ownException('E')
except ownException as e:
    print(e)
    pass
"""
先自定义了一个异常。
程序运行时，执行try语句，遇到“raise”，则表示碰到自定义异常（会执行所定义的异常），
此时，执行except，根据raise语句中的参数，来判断自定义异常所要执行的内容。
"""

#eg.判断输入字符串的长度，如果小于指定的长度就报错
def example():
    class shortInputException(Exception):
        def __init__(self,length,least_length):
            super().__init__()
            self.length = length
            self.least_length = least_length

        def __str__(self):  #可用来定义自定义异常发生后所要执行的内容
            return "你输入的长度为{}，最短长度为{}".format(self.length,self.least_length)

    try:
        a = input('请输入内容：')
        if len(a) < 10:
            raise shortInputException(len(a),10)
        else:
            print("符合要求")
    except shortInputException as e:
        print("前")
        print(e)
        print("后")

example()















        
