#!/usr/bin/python3.7
#Filename:水仙花数1.py

#每位数的3次方之和等于本身这个数（153 = 1**3 + 5**3 +3**3）

for n in range(100,1000):
    a = n%10        #个位数
    b = n//10%10    #十位数
    c = n//100      #百位数
    if n == a**3 + b**3 + c**3:
        print(n)

print('Done')
