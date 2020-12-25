#python3.7
#Filename:转换.py

def c():    #元组内只能有且必须有两个元素，第一个为键，第二个为值
    """
    元组转字典
    """
    a = (1,2)
    b = ("q","w")
    
    c1 = dict([a,b])    #dict([元组1、元组2、···])，元组内有且只有两个元素，且需注意变成字典后键不能相同
    c2 = dict([a])
    c3 = dict([(6,9)])
    print(c1,c2,c3)

def d():
    """
    元组转列表
    """
    a = (1,2)
    b = ("q","w")
    d0 = (1,2,"q","6")
    
    d1 = list(a)    #list(元组)
    d2 = list(b)
    d3 = list(d0)
    #d4 = list(a,b)     #错误。括号内只能含有一个元组项目
    print(d1,d2,d3)

def e():
    """
    列表转元组
    """
    a = [1,2,3]
    b = ["q",6]

    e1 = tuple(a)
    e2 = tuple(b)
    #e3 = tuple(a,b)    #错误。与list()相同，只能含有一个项目
    print(e1,e2)

def f():
    """
    字典转元组或列表
    """
    a = {1:2,"q":"w",6:"p"}

    f1 = list(a)    #元组就用tuple。括号内没有指定时，默认返回由键组成的列表(元组)
    f2 = list(a.keys())
    f3 = list(a.values())
    f4 = list(a.items())    #注意它的返回格式
    print(f1,f2,f3,f4)

def g():
    """
    ...转集合
    """
    a = (1,2,3,4,6,3,1)
    b = ["q","w","e","w"]
    c = {1:2,"q":"w",6:2}

    g1 = set(a)
    g2 = set(b)
    print(g1,g2)

    g3 = set(c)     #没有指定时，默认选择键来返回
    g4 = set(c.keys())
    g5 = set(c.values())
    g6 = set(c.items())
    print(g3,g4,g5,g6)

def h():
    """
    集合转元组或列表
    """
    a = {1,2,3,6,2}     #会先将集合去重，再执行转换

    h1 = list(a)    #或tuple
    print(h1)


if __name__ ==  "__main__":
    print(h.__doc__)
    h()
print("Done")
