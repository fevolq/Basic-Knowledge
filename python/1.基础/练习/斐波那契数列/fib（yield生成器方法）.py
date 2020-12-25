#python3.7
#Filename:斐波那契数列.py

x,y = 0,1

def fib():
    global x,y
    while y<100:
        f = yield y
        x,y = y,x+y

for i in fib():
    print(i,end=" ")

