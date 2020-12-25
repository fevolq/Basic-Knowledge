#!python3.7
#Filename:test2.py

def get_num(num):
    """
    num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表
    """
    l = []
    n = []
    for i in num:
        if isinstance(i,int):   #判断i的类型
            if i&1 == 0:
                l.append(i)
        else:
            n.append(i)
    if len(n) == 0:
        return "全是数字，偶数列表为：",l
    else:
        return "不全是数字，偶数列表为：",l

#print(get_num([1,2,3,4,5,6]))
#print(get_num(["a","bd","12",65]))
#print(get_num(["12",65,66]))

def func(*f):
    """
    引入任意多的列表参数，返回所有列表中最大的那个元素
    """
    #print(f)
    a = []
    for i in range(len(f)):
        a = a + f[i]
    a.sort()
    return a[-1]

#print(func([1,2,3],[9,6,2],[0,3,0]))

def get_dir(f):
    """
    f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"
    """
    import os
    for a,b,c in os.walk(f):
        if len(b)== 0:
            return "没有文件夹"
        else:
            return b

#print(get_dir("C:\\Users\\15394\\Desktop\\python教程\\python入门"))
#print(get_dir("C:\\Users\\15394\\Desktop\\python教程\\python"))

"""
print(func.__code__)        #返回这个函数所在文件的路径以及函数在文件内的行数
print(func.__code__.co_varnames)    #返回这个函数内定义的所有变量
print(func.__code__.co_filename)    #返回这个函数所在文件的路径
"""
