#python3.7
#Filename:Python中单线程、多线程和多进程的效率对比实验.py

import requests
import time
from threading import Thread
from multiprocessing import Process

def cpu():
    """CPU密集操作"""
    def count(x, y):
        # 使程序完成50万计算
        c = 0
        while c < 500000:
            c += 1
            x += x
            y += y

    print("线性：")
    t = time.time()
    for x in range(10):
        count(1, 1)
    print("Line cpu", time.time() - t)

    print("\n多线程：")
    counts = []
    t = time.time()
    for x in range(10):
        thread = Thread(target=count, args=(1,1))
        counts.append(thread)
        thread.start()
    while True:
        e = len(counts)
        for th in counts:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print(time.time() - t)

    print("\n多进程：")
    counts = []
    t = time.time()
    for x in range(10):
        process = Process(target=count, args=(1,1))
        counts.append(process)
        process.start()
    while True:
        e = len(counts)
        for th in counts:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print("Multiprocess cpu", time.time() - t)

def io():
    """IO密集操作"""
    def write():
        f = open("test.txt", "w")
        for x in range(5000000):
            f.write("testwrite\n")
        f.close()
    def read():
        f = open("test.txt", "r")
        lines = f.readlines()
        f.close()

    print("线性：")
    t = time.time()
    for x in range(10):
        write()
        read()
    print("Line IO", time.time() - t)

    print("\n多线程：")
    def io():
        write()
        read()
 
    t = time.time()
    ios = []
    t = time.time()
    for x in range(10):
        thread = Thread(target=count, args=(1,1))
        ios.append(thread)
        thread.start() 
    while True:
        e = len(ios)
        for th in ios:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print(time.time() - t)

    print("\n多进程：")
    t = time.time()
    ios = []
    t = time.time()
    for x in range(10):
        process = Process(target=io)
        ios.append(process)
        process.start()
    while True:
        e = len(ios)
        for th in ios:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print("Multiprocess IO", time.time() - t)
 

def http():
    """网络请求密集型操作"""
    _head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    url = "http://www.tieba.com"
    def http_request():
        try:
            webPage = requests.get(url, headers=_head)
            html = webPage.text
            return {"context": html}
        except Exception as e:
            return {"error": e}

    print("线性：")
    t = time.time()
    for x in range(10):
        http_request()
    print("Line Http Request", time.time() - t)

    print("\n多线程：")
    t = time.time()
    ios = []
    t = time.time()
    for x in range(10):
        thread = Thread(target=http_request)
        ios.append(thread)
        thread.start()
    while True:
        e = len(ios)
        for th in ios:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print("Thread Http Request", time.time() - t)

    print("\n多进程：")
    t = time.time()
    httprs = []
    t = time.time()
    for x in range(10):
        process = Process(target=http_request)
        ios.append(process)
        process.start() 
    while True:
        e = len(httprs)
        for th in httprs:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    print("Multiprocess Http Request", time.time() - t)

if __name__ == "__main__":
    http()
    print("Done")

"""
1.如果多线程的进程是CPU密集型的，那多线程并不能有多少效率上的提升，相反还可能会因为线程的频繁切换，导致效率下降，推荐使用多进程；如果是IO密集型，多线程进程可以利用IO阻塞等待时的空闲时间执行其他线程，提升效率。
2.多线程在IO密集型的操作下似乎也没有很大的优势（也许IO操作的任务再繁重一些就能体现出优势），在CPU密集型的操作下明显地比单线程线性执行性能更差，但是对于网络请求这种忙等阻塞线程的操作，多线程的优势便非常显著了
3.多进程无论是在CPU密集型还是IO密集型以及网络请求密集型（经常发生线程阻塞的操作）中，都能体现出性能的优势。不过在类似网络请求密集型的操作上，与多线程相差无几，但却更占用CPU等资源，所以对于这种情况下，我们可以选择多线程来执行
"""

#CPU密集型（计算较多）使用多进程，IO密集型（读写文件较多）使用多线程
#网络请求密集型（请求网络内容）使用多线程。（与多进程差不多，但多进程更耗cpu）

