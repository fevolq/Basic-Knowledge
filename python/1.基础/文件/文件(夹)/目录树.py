#!/usr/bin/python3.7
#Filename:目录树.py

#向os.walk()传递要返回目录树的目录
#要打断程序（停止继续运行搜索）    按Ctrl + C

import os
for folderName,subfolders,filenames in os.walk("F:\\教程\\python"):     #每次更改目录时要\\
    print("当前文件夹名",folderName)

    for subfolder in subfolders:
        print("包含的文件夹名",folderName,":",subfolder)

    for filename in filenames:
        print("包含的文件名",folderName,":",filename)

    print("\n")

"""
os.walk()函数在循环迭代中，每次迭代返回三个值：

1.当前文件夹名称的字符串
2.当前文件夹中文件夹的字符串列表
3.当前文件夹中文件的字符串列表
"""

#C:\\Users\\15394\\Desktop

#每一个文件夹是一个节点，向上延伸，连接该文件夹内部的文件（夹），
#当一条支路走完，再从最内部节点的父节点的第二个文件夹(若存在)往上跑，以此类推
