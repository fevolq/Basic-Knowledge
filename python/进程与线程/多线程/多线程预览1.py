#!/usr/bin/python3.7
#Filename:多线程预览1.py

#内置的threading模块

import threading
import time

exitFlag = 0

class myThread(threading.Thread):           #继承类
    def __init__(self,threadID,name,delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name,self.delay,5)     #即在线程内需要执行的操作（运行下方函数）
        print("退出线程：" + self.name)

#为线程定义一个函数
def print_time(threadName,delay,counter):   #此时counter在上面的类的run里已经定义为常数5
    while counter:
        #if exitFlag:
            #threadName.exit()
        time.sleep(delay)
        print("{}:{},{}".format(threadName,666,time.ctime(time.time())))
        counter -= 1

#创建线程
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

#开启新线程
thread1.start()
thread1.join()      #join在这时，线程1结束后再执行线程2
thread2.start()
#thread1.join()     #join()的位置不同，线程的运行方式也有所不同
thread2.join()

print("退出主线程")

"""
run(): 用以表示线程活动的方法，即线程需要执行的操作。
start():启动线程活动。
join([time]): 等待至线程中止才会进行下一步操作。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的(True/False)。
getName(): 返回线程名。
setName(): 设置线程名
"""
