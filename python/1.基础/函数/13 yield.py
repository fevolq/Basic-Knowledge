#python3.7
#Filename:yield生成器1.py

#包含yield的函数，是一个可迭代对象
#函数每次跑到yield时就会停止往下运行函数的部分，等到下次再次运行函数时，直接从此处继续往下运行

#send()的问题思考

def a1():
    a = [0,1,2,3]
    for i in a:
        print(i)

def a2():
    def test2():
        i,a = 0,4
        while i<a:
            x = yield i     #yield是一个生成器，用于迭代，不能用return代替
            print(x)            #并不是把i赋值给x，若要给x传值，需要使用send()方法
            i +=1
            
    print(test2())
    for i in test2():
        print(i)

def a3():           #异常
    def test3():
        i,a = 0,4
        while i<a:
            yield i
            i += 1
    t = test3()
    print(next(t))     #返回第一个yield的生成
    print(next(t))     #返回第二个yield的生成
    print(next(t))
    print(next(t))
    #print(next(t))     #函数的迭代在上一步已经跑完，所以此步异常     

def a4():
    def test4(n):
        for i in range(n):
            print('...')
            x = yield i     #yield是一个生成器，用于迭代，不能用return代替
            print('!!!')
            print('x：',x)            #并不是把i赋值给x，若要给x传值，需要使用send()方法
            print('***')
            #i +=1
            
    t = test4(6)
    for i in t:
        print('----')
        print(t.send(666))

a4()

"""
1、对于生成器，当调用函数next(generator)时，将获得生成器yield后面表达式的值；
2、当生成器已经执行完毕时，再次调用next函数，生成器会抛出StopIteration异常；
3、当生成器内部执行到return语句时，自动抛出StopIteration异常，return的值将作为异常的解释；
4、外部可以通过generator.close()函数手动关闭生成器，此后调用next或者send方法将抛出异常
"""










