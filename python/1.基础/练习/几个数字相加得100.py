#!/usr/bin/python
# Filename：hundred.py

#用1、2、3来相加得到100有多少种方法

i = 0
for x in range(0,101):
    for y in range(0,51):
        for z in range(0,34):
            if 100 == 1*x + 2*y + 3*z:
                i = i + 1       #i += 1
            
print("一共有{}种方法".format(i))

