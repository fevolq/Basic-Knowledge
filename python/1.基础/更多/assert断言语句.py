#!/usr/bin/python
#Filename:assert.py

#assert语句用来声明某个条件是真的。
# 断言：一个会抛出异常的判断,这个条件一旦成立就成立了，一旦不成立就报错了,就都不执行下面的了

list = [1]
assert len(list) >= 1
print(list.pop())       #pop(i)，去除掉列表中的指定位置的对象并返回这个值，当括号内为空时，默认去除最后一个。


#assert len(list) >= 1          #此步会引发一个错误

#例如，如果某个列表中有唯一一个元素，而想要检验这一点，并在它非真时引发一个错误，可使用assert语句。
