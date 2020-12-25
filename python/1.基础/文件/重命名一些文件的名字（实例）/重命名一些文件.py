#!/usr/bin/python3.7
#Filename:重命名一些文件.py

#将文件名中的日期进行更改（月-日-年 改为 日-月-年）

import re,shutil,os

#正则
nameRe = re.compile(r"""
    (.*?)              #日期前可能存在的名字
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$            #日期后可能存在的名字
    """,re.VERBOSE
    )

a = os.listdir(".")     #返回当前路径中包含的内容（即要处理的文件）的绝对路径字符串列表）
#print(a)
for oldName in a:
    b = nameRe.search(oldName)
    if b == None:
        continue
    else:
        before = b.group(1)
        month = b.group(2)      #根据正则表达式中的左括号来判断是第几组
        date = b.group(4)
        year = b.group(6)
        after = b.group(8)

    newName = before + date + "-" + month + "-" + year + after
    """
    workingDir = os.path.abspath(".")   #绝对路径，返回当前路径（绝对路径）的字符串
    oldName = os.path.join(workingDir,oldName)
    newName = os.path.join(workingDir,newName)
    """
    print("将{}更名为{}".format(oldName,newName))
    
    #shutil.move(oldName,newName)       #进行更改的操作，运行时消除注释
    
