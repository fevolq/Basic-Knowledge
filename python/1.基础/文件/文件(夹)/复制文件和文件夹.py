#!/usr/bin/python3.7
#Filename:复制文件和文件夹.py

#此程序只用来参考，尽量不运行
#若要运行此程序，需在桌面先新建所需的文件和文件夹（见最后注释）

import shutil,os
os.chdir("C:\\Users\\15394\\Desktop")   #使当前工作的路径为桌面

class Copy:
    #将文件复制到另一文件夹中，名字相同
    #shutil.copy("C:\\Users\\15394\\Desktop\\新建文本文档.txt","C:\\Users\\15394\\Desktop\\新建文件夹")     #复制到文件夹中时，该文件夹需已存在

    #将单个文件复制到另一文件夹中，名字另取(123)
    #shutil.copy("C:\\Users\\15394\\Desktop\\新建文本文档.txt","C:\\Users\\15394\\Desktop\\新建文件夹\\123.txt")    #后缀名需相同

    #将文件夹（包括其内容）复制到另一文件夹内
    #shutil.copytree("C:\\Users\\15394\\Desktop\\新建文件夹2","C:\\Users\\15394\\Desktop\\新建文件夹\\666")    #将文件夹（包括内容）一起复制到指定的文件夹，且该文件夹还不存在(未创建)


class Move:     #移动和重命名文件（夹）
    #移动文件（若目标文件夹中已存在此同名文件，则会异常）
    #shutil.move("C:\\Users\\15394\\Desktop\\新建文本文档.txt","C:\\Users\\15394\\Desktop\\新建文件夹")

    #移动文件（名字另取）
    #shutil.move("C:\\Users\\15394\\Desktop\\新建文本文档.txt","C:\\Users\\15394\\Desktop\\新建文件夹\\123.txt")   
    #若目标处没有该文件夹（没有新建文件夹），则会异常。移动重命名时，若没有后缀，则会在目标文件夹内变成一个没有后缀的文件

    #移动文件夹
    #shutil.move("C:\\Users\\15394\\Desktop\\新建文件夹 (2)","C:\\Users\\15394\\Desktop\\新建文件夹")  #连带内容一起移动
    #移动文件夹（名字另取，需目标处没有该名字的文件夹）
    #shutil.move("C:\\Users\\15394\\Desktop\\新建文件夹 (2)","C:\\Users\\15394\\Desktop\\新建文件夹\\123")
    

class Rm:   #均永久删除，不可逆（不在回收站）
    #os模块能删除单个文件或单个空文件夹
    #shutil内置模块删除文件夹及其所有内容
    
    #os.unlink("C:\\Users\\15394\\Desktop\\新建文本文档.txt")      #删除单个文件
    #os.rmdir("C:\\Users\\15394\\Desktop\\新建文件夹")            #删除单个空文件夹

    #shutil.rmtree("C:\\Users\\15394\\Desktop\\新建文件夹 (2)")       #删除文件夹（其内可包含内容）
 
print("Done")


"""
copy：在桌面新建：新建文本文档(包含内容)、新建文件夹、新建文件夹2(包含内容)，其余根据命令自行处理
move：在桌面新建：新建文本文档、新建文件夹、新建文件夹2(包含内容)，其余根据命令自行处理
rm：在桌面新建：新建文本文档、新建文件夹、新建文件夹2(包含内容)
"""
