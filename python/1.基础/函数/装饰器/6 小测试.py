#python3.7
#Filename:小测试.py

"""
写一个装饰器，传入一个秒数，
如果函数执行完成超过这个数值，则显示bad，否则显示good
"""

import functools
import time

def warp(x):
    def decorator(func):
        @functools.wraps(func)
        def wraps(*args,**kwargs):
            start_time = time.time()
            res = func(*args,**kwargs)
            end_time = time.time()
            times = end_time - start_time   #执行函数花费的时间
            if times>x:
                print("bad")
            else:
                print("good")
            print("使用了%s秒"%times)
            return res
        return wraps
    return decorator

@warp(2)    #传入的秒数为2秒
def function(x,y):
    """原始函数"""
    for i in range(x):
        y = y+i
        time.sleep(0.5)
    return y

print(function(5,0))

