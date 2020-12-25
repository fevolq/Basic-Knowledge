#python3.7
#Filename:list排序.py

#list.sort()只能对列表排序，而sorted()对所有可迭代序列都有效
#list.sort()直接改变原列表，sorted()返回一个排好序的新列表

#key参数的值是一个函数，这个函数只能有一个返回值，且用返回值来进行比较。
#reverse为True时，则降序排列；默认为False时，升序排列。（升序：数字变大，字母a到z）
#稳定性：当多个元素有相同的key时（即拥有相同的排序标准），则排序前后他们的先后顺序不变（不论升降排序，都按原先顺序）
#复杂性：在稳定性的基础上（即相同key），改变key（改变lambda的返回值）


#使用list内置的sort排序,直接改变列表
#list.sort(key=None,reverse=False)
def a():
    l = [2,6,33,6,45,9]
    l.sort()
    print(l)
    l.sort(reverse=True)   
    print(l)
def a1():
    l = [('a',5),('th',6),('h',2),('fwrhy',9),('u',6)]
    l.sort(key=lambda x:x[1])   #x代表列表内的每个元组元素，表示以列表内的元组的第二个元素来做排序标准
    print(l)

#使用内置的sorted排序
#与sort方法类似，但sorted不改变原来的列表，并返回一个排好序的列表
def b():
    l = [2,6,33,6,45,9]
    list1 = sorted(l)   #sorted()的返回值是一个列表
    print(list1)
def b1():
    data = [{'name':'abc','score':99},{'name':'qwe','score':66},{'name':'asd','score':78},{'name':'zxc','score':66}]
    data1 = sorted(data,key=lambda x:x['score'])
    print(data1)
def b2():   #稳定性
    student_tuples = [('qwe','A',9),('abc','B',6),('zxc','A',8),('asd','B',8)]
    students = sorted(student_tuples,key=lambda x:x[1],reverse=False)
    print(students)
    studentss = sorted(student_tuples,key=lambda x:x[1],reverse=True)
    print(studentss)
def b3():   #复杂性——多级排序
    student_tuples = [('qwe','A',9),('abc','B',6),('zxc','A',8),('asd','B',8)]
    students = sorted(student_tuples,key=lambda x:(x[1],x[2]),reverse=False)    #先按第二个关键字排序，完成后再在相同的每段中(第二个关键字相同)按第三个关键字排序
    print(students)
    
if __name__ == '__main__':
    b3()
    
