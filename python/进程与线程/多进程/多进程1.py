#python3.7

import time
import random
from multiprocessing import Process

#方法1
print("方法1：")
import random
from multiprocessing import Process
def piao(name):
    print('%s piao' %name)
    time.sleep(random.randrange(1,5))
    print('%s piao end' %name)



p1=Process(target=piao,args=('e',)) #必须加,号
p2=Process(target=piao,args=('a',))
p3=Process(target=piao,args=('w',))
p4=Process(target=piao,args=('y',))

p1.start()
p2.start()
p3.start()
p4.start()
print('主线程')

###################
print("\n")
print("方法2：")
#方法2
class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s piaoing' %self.name)

        time.sleep(random.randrange(1,5))
        print('%s piao end' %self.name)

p1=Piao('e')
p2=Piao('a')
p3=Piao('w')
p4=Piao('y')

p1.start() #start会自动调用run
p2.start()
p3.start()
p4.start()
print('主线程')

###################
print("\n")
print("其他方法或属性：")
#其他方法或属性
#进程对象的其他方法一:terminate,is_alive
class Piao1(Process):
    def __init__(self,name):
        self.name=name
        super().__init__()

    def run(self):
        print('%s is piaoing' %self.name)
        time.sleep(random.randrange(1,5))
        print('%s is piao end' %self.name)


p1=Piao1('e1')
p1.start()

p1.terminate()#关闭进程,不会立即关闭,所以is_alive立刻查看的结果可能还是存活
print(p1.is_alive()) #结果为True

print('开始')
print(p1.is_alive()) #结果为False
