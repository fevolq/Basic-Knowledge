#python3.7
#Filename:文件路径.py

#注意文件目录中的“\”需要添加一个“\”来进行转义
#os.getcwd()返回当前工作路径
#os.chdir("path")将工作路径返回到path指定的路径
#os.makedirs("path")在path路径创建文件夹

import os

"""
#使用os.makedirs()创建新文件夹（目录）
os.makedirs("C:\\Users\\15394\\Desktop\\abc\\123")      #在桌面创建文件夹
"""
#使用os.path.join()为某个文件名创建字符串
a = ["abcd","123"]
for i in a:
    print(os.path.join("C:\\Users\\15394\\Desktop"),i)

#返回当前工作目录
print("当前工作目录：",os.getcwd())    #以字符串形式，返回当前文件所在的文件夹的绝对路径
import sys
print("当前文件的路径：",sys.argv)      #以列表形式，返回当前文件的绝对路径

print("\n")

#绝对路径：总是从根文件夹开始
#相对路径：相对于程序的当前工作目录
class A:
    a = "C:\\Users\\15394\\Desktop\\123.exe"
    b = "C:\\Users\\15394\\Desktop\\123"
    print("绝对路径：",os.path.dirname(a))    #绝对路径（文件所在的路径全称，不包括该文件名）
    #print("绝对路径：",os.path.dirname(b))
    print("相对路径：",os.path.basename(a))   #相对路径（即文件(夹)名）
    #print("相对路径：",os.path.basename(b))
    print("返回路径的元组：",(os.path.dirname(a),os.path.basename(a)))

    print("目录名和基本名：",os.path.split(a))  #返回目录名和基本名组成的元组，与上一步结果相同
    print("返回目录名的列表：",a.split(os.path.sep))     #以一层层的路径名为元素组成的列表

    print(os.path.getsize('F:\\教程\\python\\1.基础\\文件\\文件(夹)\\文件路径.py'))  #返回文件的字节大小
    print(os.listdir('C:\\Users\\15394\\Desktop'))      #以列表形式返回一个文件夹内的所有文件(夹)名称

print("\n")

#检查路径有效性
class B:
    path = 'F:\\教程'
    #os.path.exists(path)检查路径中的文件（夹）是否存在。若存在，返回True，否则返回False
    #os.path.isfile(path)检查路径参数存在并且是一个文件。…………
    #os.path.isdir(path)检查路径参数存在并且是一个文件夹。……………
    print(os.path.exists(path))
    print(os.path.isfile(path))
    print(os.path.isdir(path))
