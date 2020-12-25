#!/usr/bin/python
# Filename：A_modul.py

#输入数字模块

print('结束时请输入over\n')
a = []
#b = []

while True:
    math = input('输入你想要比较的数：')
    if math == 'over':
        break
    else:
                                    #b.append(math)
        #c = int(b.pop())           #c = int(b[0])
        a.append(int(math))         #a.append(c)
                                    #b.pop()
        
if __name__ == '__main__':
    print(a)

