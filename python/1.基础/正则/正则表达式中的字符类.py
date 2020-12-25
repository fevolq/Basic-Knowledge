#!/usr/bin/python3.7
#Fielname:正则表达式中的字符类匹配.py

import re

class A:    #内置的角色类
    """
    \d从0到9的任何数字；\D任何不是0到9之间的数字的字符。
    \w任何字母，数字或下划线字符（把它想象成匹配的“单词”字符,单词后有空格，所以会停止）；
        \W任何不是字母，数字或下划线字符的字符。
    \s任何空格，制表符或换行符（想象成匹配“空格”字符）；
        \S任何不是空格，制表符或换行符的字符。

    注意大小写的不同
    """
    example = re.compile(r"\d+\s\w+")   #\d+表示匹配一个或多个数字
    a = example.findall("1 apple,23 pear,4 banana,567 orange")
    #正则表达式\d+\s\w+会匹配具有一个或多个数字开头，后跟一个空格，后跟一个或多个字母/数字/下划线的文本
    print("a的匹配：",a)

print("\n")

class B:    #制作角色类
    """
    使用[]来自定义角色类。
    使用-字符来表示范围
    插入^符号来反向匹配
    """
    example1 = re.compile(r"[aeiouAEIOU]")     #匹配元音字母，不论大小写
    b1 = example1.findall("sheloveme, AI,BCD")
    print("b1的匹配：",b1)

    example2 = re.compile(r"[a-z,A-Z,1-9]")     #匹配所有数字和字母（不论大小写）
    b2 = example2.findall("sa9f1")
    print("b2的匹配：",b2)

    example3 = re.compile(r"[^aeiouAEIOU]")     #反向匹配
    b3 = example3.findall("sheloveme, AI,BCD")              #注意逗号的匹配
    print("b3的匹配（与b1比较）：",b3)

print("\n")

class C:    #匹配开头与结尾
    """
    r"^abc"表示匹配以abc开头的字符串，注意与反向匹配的差别。
    r"\d$"表示匹配以数字（0到9）结尾的字符串
    r"\d+$"表示匹配以数字0到9从开始到结尾的字符串
    """
    example1 = re.compile(r"^Hello")    #匹配以Hello开头的字符串
    c1 = example1.search("Hello World")
    print("c1的匹配：",c1.group())
    c2 = example1.search("He says Hello")
    if c2 == True:
        print("c2有匹配")
    else:
        print("c2没有匹配")

    example2 = re.compile(r"\d$")       #匹配以数字结尾
    c3 = example2.search("你的号码是56")
    print("c3的匹配：",c3.group())              #返回最后一个数字
    c4 = example2.search("你的号码是six")
    if c4 == True:
        print("c4有匹配")
    else:
        print("c4没有匹配")

    example3 = re.compile(r"\d+$")      #匹配以数字组成的字符串
    c5 = example3.search("123456")
    print("c5的匹配：",c5.group())
    c6 = example3.search("123abc46")
    if c6 == True:
        print("c6有匹配")
    else:
        print("c6没有匹配")
    c7 = example3.search("123 456")
    if c7 == True:
        print("c7有匹配")
    else:
        print("c7没有匹配")
    c8 = example3.search("abc123")
    if c8 == True:
        print("c8有匹配")
    else:
        print("c8没有匹配")

print("\n")

class D:    #通配符（.），匹配除换行符之外（空格符不属于换行符）的任何字符
    """
    用于匹配有相同字符的字符串
    注意匹配的大小写
    .代表一个字符，即r".xy"匹配三个字符，第一个可任选（除了换行符），第二三个为xy
    """
    example = re.compile(r".at")    #匹配具有at的最少包含3个字符的字符串，且只返回at字符串加上a前面的一个字符（可为空格、逗号等）
    d = example.findall("at.The cat in the hat sat on the flat mat.CAT, at,at")
    print("d的匹配：",d)
    
print("\n")

class E:    #.*匹配一切
    """
    .表示一个非转行符的字符，*表示前面一个字符的0个或多个
    .*默认为贪婪模式，即尽可能多的匹配文本。一旦被截断，则不再继续匹配后面的内容。
    .*?以非贪婪模式匹配
    """
    example1 = re.compile(r".*")
    e1 = example1.search("afg126as84hg")
    print("e1的匹配：",e1.group())
    
    example2 = re.compile(r"abc:(.*),123(.*)789")
    e2 = example2.search("abc: qwe,123456789")
    print("e2的全部匹配：",e2.group(),"\ne2的第一组匹配：",e2.group(1),"\ne2的第二组匹配:",e2.group(2))

    #贪婪与非贪婪
    example3 = re.compile(r"<.*>")      #贪婪模式
    example4 = re.compile(r"<.*?>")     #非贪婪模式
    e3 = example3.search("<abc def> qwe>")
    e4 = example4.search("<abc def> qwe>")
    print("贪婪模式e3的匹配：",e3.group(),"\n非常规模式e4的匹配：",e4.group())
    
print("\n")

class F:    #匹配所有行（即换行符也不能终止匹配）
    """
    通过re.DOTALL作为第二个参数来避免匹配截止到换行符
    """
    example1 = re.compile(r".*")            #只能匹配第一行
    example2 = re.compile(r".*",re.DOTALL)      #可以匹配所有行
    f1 = example1.search("abc\ndef\nqwe")
    f2 = example2.search("abc\ndef\nqwe")
    print("f1的匹配（截止到换行符）：",f1.group())
    print("f2的匹配（包括换行符）：",f2.group())

print("\nDone")

#re.VERBOSE作为第二个参数传递给compile()，用来忽略正则表达式里的空格和注释
