#!python3.7
#Filename:test1.py

def many(*x):
    """
引入任意多的字符串参数，结果返回（长度）最长的字符串
    """
    #print(x)
    y = list(x)
    #print(y)
    li = [(m,len(m)) for m in y]
    #print(li)
    li.sort(key=lambda i:i[1])
    return "最短：{}， 最长：{}".format(li[0][0],li[-1][0])

#print(many("af","218664","gsha"))
    
def get_text(f):
    """
f参数为任意一个文件的磁盘路径，该函数返回f文件的内容
    """
    with open(f,"r") as x:
        y = x.readlines()
        Read = "".join(y)
    return Read

#print(get_text("F:\\教程\\python\\1.基础\\函数\\一些练习\\test1.txt"))


def get_dir(folder):
    """
folder参数为任意一个文件夹路径，该函数返回folder文件夹的文件列表
    """
    import os
    for folderName,folders,filenames in os.walk(folder):
        l = folders + filenames
        return l

#print(get_dir("F:\\教程\\python"))
"""
folderName：文件夹的名字（和路径）
folders：文件夹内部的文件夹名称（以列表形式返回）
filenames：文件夹内部的文件名称（以列表形式返回）
"""
