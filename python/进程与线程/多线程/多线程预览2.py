#python3.7
#Filename:多线程预览2.py

import threading,time

def test(t):
    print(t)

l = []

for i in range(6):
    th = threading.Thread(target=test,args=[i])     #创建一个线程，target表示线程要执行的操作，args表示传递的变量（若函数没有变量，则不需要）
    th.start()      #运行线程
    l.append(th)
    time.sleep(0.5)   #延迟，以便进行观察

#for i in l:
#    i.join()       #用以使下面的在上面的线程完成后再运行

print("主部")

"""
创造一个进程时，会创造一个线程，这个线程被称为主线程
一个进程只有一个主线程
python的多线程，不是真正意义上的多线程
"""
