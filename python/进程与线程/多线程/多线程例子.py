#python3.7
#Filename:多线程例子.py

#有10个刷卡机，代表建立10个线程，每个刷卡机每次扣除用户一块钱进入总账中，每个刷卡机每天一共被刷100次。账户原有500块。所以当天最后的总账应该为1500

import threading

loc = threading.Lock()

num = 500

def sum1():
    global num
    loc.acquire()           #加锁
    for i in range(100):
        num += 1
    print(num)
    loc.release()           #释放

for i in range(10):     
    a = threading.Thread(target=sum1)
    b = threading.Thread(target=sum1)   #只测试锁机制时，可注释掉b
    a.start()
    b.start()   #
    a.join()

print("最后是：",num+1)     #=1用来测试a.join()后的运行顺序

#多线程中，若要避免一个变量同时被多个线程进行更改，可使用锁操作
#加锁一定要释放，否则会变成死锁，会出错
