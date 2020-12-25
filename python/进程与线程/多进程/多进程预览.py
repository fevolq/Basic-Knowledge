#python3.7
#注意：要在cmd下运行，IDE输出窗口输出的主进程的内容，我们创建的进程p不是主进程，所以无输出。
#       创建进程及执行代码要在：if __name__ == "__main__": 后面

import multiprocessing
from multiprocessing import Process, Pool
import os
import time


def run_proc(wTime):
    n = 0
    while n < 3:
        print("subProcess %s run," % os.getpid(),"{0}".format(time.ctime()))  #获取当前进程号和正在运行是的时间
        time.sleep(wTime)    #等待（休眠）
        n += 1

if __name__ == "__main__": 
    p = Process(target=run_proc,args=(2,))  #申请子进程
    p.start()     #运行进程
    p.join()
    print("Parent process run. subProcess is ", p.pid)
    print("Parent process end,{0}".format(time.ctime()))

"""
Python中提供了multiprocessing这个包实现多进程。multiprocessing支持子进程、进程间的同步与通信，提供了Process、Queue、Pipe、Lock等组件。

multiprocessing中提供了Process类来生成进程实例
Process([group [, target [, name [, args [, kwargs]]]]])

参数介绍：
group分组，实际上不使用
target表示调用对象，你可以传入方法的名字
args表示给调用对象以元组的形式提供参数，比如target是函数a，他有两个参数m，n，那么该参数为args=(m, n)即可
kwargs表示调用对象的字典
name是别名，相当于给这个进程取一个名字

方法介绍：
p.start()：启动进程，并调用该子进程中的p.run() 
p.run():进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法  
p.terminate():强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁
p.is_alive():如果p仍然运行，返回True
p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间，需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程

属性介绍：
p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start()之前设置
p.name:进程的名称
p.pid：进程的pid
p.exitcode:进程在运行时为None、如果为–N，表示被信号N结束(了解即可)
p.authkey:进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）

"""
