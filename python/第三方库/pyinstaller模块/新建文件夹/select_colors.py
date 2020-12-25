#!-*-coding:utf-8 -*-
#!python3.7
#!@Author：fuq666@qq.com
#!Filename:

import random

colors = ['yellow', 'red', 'black', 'blue', 'cyan', 'magenta', ]

color1 = random.choice(colors)
colors.remove(color1)       #没有返回对象（或者说为None）
color2 = random.choice(colors)

if __name__ == '__main__':
    print(color1,color2)