#python3.7
#Filename:断言.py

#assert()方法，断言成功，则程序继续执行，断言失败，则程序报错

a = 3
assert(a>1)
print('断言成功，继续执行')

"""
b = 6
assert(b>9)
print('断言失败')
"""

c = 6
try:
    assert(c>9)
    print('断言成功')
except:
    print('断言失败')
