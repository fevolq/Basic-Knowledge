#!/usr/bin/python3.7
#Filename:剥离头尾字符.py

#strip()只会剥离两侧的字符
#strip()默认会剥离前后两边的空格；lstrip()剥离左边；rstrip()剥离右边

a = "  He llo  "
print(a.strip())
print(a.lstrip())
print(a.rstrip())
    

b = "12a12b12c13d12"
print(b.strip("12"))    #剥离指定字符

c = "aabc666abc666bcabac"
print(c.strip("abc"))    #传入多个字符参数时，不管传入的参数是什么排列形式，都会拆解成一个个字符，然后把头尾的这些字符去掉
