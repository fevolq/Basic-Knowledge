#!/usr/bin/python
# Filename：输出格式化（定制输出）.py

age = 25
name = 'a'

print('%s的年龄是%s'%(name,age))
print('%s的年龄是%d'%(name,age))

print('%s在学习python'%name)

#print语句可以使用跟着%的项目元组的字符串，具备定制功能
#%s表示字符串，%d表示整数
#元组必须按照输出的相同顺序来对应,定制只有一个项目时，可以不用括号


print()

#注意{}的用法
print("{}：{}，{}".format(1,2,"a"))       #{}括号及其里面的字符（称作格式化字段）
                                          #会被format()中的参数替换

print("\n{0}和{1}".format("a","b"))      #括号中的数字用于指向传入对象在format()中的位置，从0开始
print("{1}和{0}".format("a","b"))

print("\n{a}和{b}".format(a=0,b="我"))    #可用关键字参数
print("{0}和{1}和{a}".format("a",9,a=2))  #位置和关键字参数可以结合使用
