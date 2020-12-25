#python3.7
#Filename:文件内光标移动.py

import time

with open('光标移动.txt','rb') as f:
    f.seek(1,0)
    print('当前指针的位置：{}\n'.format(f.tell()))
    while True:
        line = f.readline()
        if line:
            print(line)
            #print(line.decode('utf-8'))
        else:
            time.sleep(0.2)

print("Done")

'''
文件指针移动(以字节为单位)：seek
file.seek(value,mode)  //value为移动的单位(字节)，mode为移动的类型(0:文件开始，1:当前位置，2:文件末尾)
file.tell()   //获取当前文件指针的位置
'''
"""
txt文件内容为
123
4567

qw
呵
666
"""
