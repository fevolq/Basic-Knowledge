# 创建装饰器， 要求如下：
# 1. 创建add_log装饰器， 被装饰的函数打印日志信息；
# 2. 日志格式为: [字符串时间] 函数名: xxx， 运行时间：xxx, 运行返回值结果:xxx

import functools
import time

def log(kind):  # kind="debug"，日志类型
    def add_log(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = fun(*args, **kwargs)
            end_time = time.time()
            print("<%s> [%s] 函数名: %s， 运行时间：%.5f, 运行返回值结果:%d"
                  %(kind, time.ctime(), fun.__name__, end_time-start_time, res )
                  )
            return res
        return wrapper
    return  add_log
@log("debug")
#  log("debug")==> 返回值是add_log
#  add=add_log(add)
def add(x,y):
    time.sleep(0.1)
    return x+y

#print(add(14214124124,1241231231313))  #会打印res的值，即装饰器的返回值
add(14214124124,1241231231313)
