#!/usr/bin/python3.7
#Filename:random生成随机数.py

#random每次随机取得都不相同（即每次的运行结果都是随机的）

import random

a = ["苹果","banana","梨子","橙子","菠萝"]
print(random.choice(a))     #随机从一个列表内里取一个

b = random.randrange(9)     #随机从一个数字范围内取一个
print(b)

b1 = random.randint(10,20)  #随机整数
print(b1)

b2 = random.random()        #不能传参数值，返回0—1随机小数
print(b2)

import numpy as np
b3 = np.random.randn(5)     #5个随机小数，以列表形式返回
print(b3)

c = random.sample(range(50),6)      #随机从给定的范围（50）内取指定数量（6）的数。
print(c)

d = random.sample(a,3)
print(d)

e = a[:]
random.shuffle(e)           #随机打乱
print(e)


#choice、randrange、sample都有返回值，而shuffle只是改变本身，没有返回值。
