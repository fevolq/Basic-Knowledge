#!-*-coding:utf-8 -*-
# python3.7
# @Author:fuq666@qq.com
# Update time:
# Filename:调用资源管理器选择路径或文件

'''
如：要保存一个文件时，想要用户自主选择保存路径时使用
'''

import tkinter as tk
from tkinter import filedialog

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

Folderpath = filedialog.askdirectory() #获得选择好的文件夹
# Filepath = filedialog.askopenfilename() #获得选择好的文件

print('选择的文件夹的路径为：',Folderpath)
# print('选择的文件的路径为:',Filepath)

# path = 'C:/Users/15394/Desktop'
with open(Folderpath+'/1.txt','w') as f:
    f.write('qwe')
    print('\nDone')