#!/usr/bin/python3.7
#Filename:更多模式的匹配.py

import re

class A:    #用括号分组
    """
    第一组括号是组1，第二组括号是组2。
    通过将整数1、2传递给group()内来匹配对象。为0或不传递则默认返回整个匹配文本。
    """
    phoneNumber = re.compile(r"(\d\d\d)-(\d{3}-\d{4})")     # \d{3}表示将\d重复3次
    a = phoneNumber.search("电话号码是123-456-7890")

    print("a第一组的输出：",a.group(1))   #返回第一个括号内的匹配
    print("a第二组的输出：",a.group(2))
    #print("a第二组的输出：",a.group(3))————有异常
    print("a全部文本的输出：",a.group())
    print("a全部组的输出：",a.groups())      #groups()一次检索所有组，以元组形式返回
    '''
    a1,a2 = phoneNumber.groups()    #当返回多个组时，可用多重赋值技巧将每个值分配给的单独的变量
    print(a1,"   ",a2)
    有异常
    '''
    
print("\n\n")

class B:    #管道匹配“|”
    """
    “|”称为管道。在想要匹配多个表达式时使用。
    如：r"ab|cd"表达式将匹配“ab”或“cd”
    """
    name = re.compile(r"abc|123")   #匹配abc或123
    b1 = name.search("abcdju")
    b2 = name.search("123789a")
    print("b1匹配：",b1.group(),"\nb2匹配：",b2.group())

    name1 = re.compile(r"abc(def|qwe|789)")     #匹配abcsef或abcqwe或abc789。
                                                #指定相同前缀一次，其余用括号包含
    b3 = name1.search("abc123ab789abcqwedhuoa451")
    print("b3全文匹配：",b3.group())
    print("b3组内匹配：",b3.group(1))      #由于正则表达式只有一个括号，所以只能到1。而且匹配括号内的内容（没有前缀）


print("\n\n")

class C:    #与？或*或+匹配
     """
    ?字符表示其前面的组（即括号内）作为可选部分。匹配0个或1个
    *字符表示其前面的组作为可选部分。匹配0个或1个或多个
    +字符表示其前面的组出现1次或多次。匹配1个或多个
    """
     name = re.compile(r"(c66)?qwe")       #表示c66是可选择的（0个或1个）
     c1 = name.search("abqweerrx45")
     c2 = name.search("abc66qweerrx45")
     print("c1的匹配：",c1.group(),"\nc2的匹配：",c2.group())

     name1 = re.compile(r"(ab)*cd6")         #表示ab是可选择的(0个或以上)
     c3 = name1.search("cd6errd9ab")
     c4 = name1.search("abcd6errd9ab")
     c5 = name1.search("abababcd6errd9ab")
     print("c3的匹配：",c3.group(),"\nc4的匹配：",c4.group(),"\nc5的匹配：",c5.group())

     name2 = re.compile(r"(op)+qwe")       #(op)+表示匹配一个或多个op
     c6 = name2.search("abopqweerrx45")
     c7 = name2.search("abopopopqweerrx45")
     print("c6的匹配：",c6.group(),"\nc7的匹配：",c7.group())


print("\n\n")

class D:    #(i){x,y}匹配特定次数
    """
    匹配其前面的组x到y次（如：x,y=2,4，则匹配2或3或4次）
    可省略x或y（保留逗号），以保留最小或最大无界限的匹配。
    {2,}2次至更多，{,5}0次至5次。
    {n}匹配n次
    """
    name = re.compile(r"(ha){3}")       
    d1 = name.search("abchahahaha123")
    print("d1的匹配：",d1.group())

    name1 = re.compile(r"(ha){2,4}")    #贪婪匹配：即默认匹配拥有的最长的字符串（要在指定范围）
    d2 = name1.search("abchahaha123")
    d3 = name1.search("abcha123")           #只有一个，不在范围内，不匹配
    print("d2的匹配：",d2.group())
    if d3 == None:
        print("d3不匹配")

    name2 = re.compile(r"(ha){2,4}?")   #非贪婪匹配：默认匹配范围内最小的字符串
    d4 = name2.search("abchahaha123")
    print("d4的匹配（与d2对比）：",d4.group())
    

print("\n\n")

class E:    #findall()方法 —— 返回所有匹配
    """
    search()方法只能返回第一个匹配的对象，而findall()将返回每个匹配对象。
    只要正则表达式中没有组，就不会返回match对象，而是返回字符串列表，列表中的
        每个字符串元素都是匹配出的一部分。
    正则表达式中有组，则返回元组列表（以元组为元素的列表），每个元组代表一个找出的匹配，且元组内的元素由正则表达式里的匹配取得。
    """
    number = re.compile(r"\d{3}-\d{3}-\d{4}")
    number1 = re.compile(r"(\d{3})-(\d{3})-(\d{4})")

    e1 = number.search("电话1：123-456-7890，电话2：789-456-1230")
    e2 = number.findall("电话1：123-456-7890，电话2：789-456-1230")
    e3 = number.findall("电话1：123-456-7890")
    e4 = number1.findall("电话1：123-456-7890，电话2：789-456-1230")

    #search()返回的是字符串，所以有group()。
    #findall()返回的是一个列表，没有group()。
    print("e1的匹配：",e1.group(),"\ne2的匹配：",e2,"\ne3的匹配：",e3,"\ne4的匹配：",e4)
    
