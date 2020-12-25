#!/usr/bin/python3.7
#Filename:压缩.py

#此程序运行需要一些程序中必备的文件

import zipfile,os
os.chdir("C:\\Users\\15394\\Desktop")

exampleZip = zipfile.ZipFile("123.zip")

print(exampleZip.namelist())   #返回zip文件内所有文件（夹）的字符串列表

exampleZip.extractall()     #将zip文件解压至当前目录的文件夹中。也可在括号内给定地址来解压，若地址处没有该文件夹，则会新建一个该文件夹

#exampleZip.extract("新建文本文档.txt")    #提取单个文件
exampleZip.close()


#创建zip文件
newZip = zipfile.ZipFile("new.zip","w")         #w代表擦除zip内现有的，重新写入。
newZip.write("1234.txt",compress_type = zipfile.ZIP_DEFLATED)
newZip.close()

newZip1 = zipfile.ZipFile("new.zip","a")        #a代表直接在zip内直接新增
newZip1.write("12345.txt",compress_type = zipfile.ZIP_DEFLATED)
newZip1.close()
