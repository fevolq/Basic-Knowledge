import os,shutil

path = r'C:\Users\15394\Desktop\新建文件夹 (2)'
l = os.listdir(path)
#print(l)

workdir = os.path.abspath(path)

for i in l:
    oldname = os.path.join(workdir,i)
    old = i[0:-5]
    print(old)
    new = old + '.mp3'
    newname = os.path.join(workdir,new)
    shutil.move(oldname,newname)
