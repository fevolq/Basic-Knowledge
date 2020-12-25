#!/usr/bin/python3.7
#Filename:水仙花数2.py

for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            a = x*100 + y*10 + z
            b = x**3 + y**3 +z**3
            if a == b:
                print("%d%d%d"%(x,y,z))

print("Done")
        
