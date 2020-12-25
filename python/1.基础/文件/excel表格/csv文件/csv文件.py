#!python3.7
#Filename:csv文件.py

import os,csv
os.chdir("C:\\Users\\15394\\Desktop")   #根据文件所在路径进行更改

eFile = open("123.csv")
eReader = csv.reader(eFile)
eData = list(eReader)
print(eData)

print(eData[1][2])

