#python3.7
#Filename:一些常用的情况.py

import datetime
import time

#直接返回当前时间（字符串）
def nowtime():
    print(datetime.datetime.now())      #2019-07-07 23:41:52.655522     datetime.datetime格式
    print(datetime.datetime.today())    #2019-07-08 09:31:13.939685     datetime.datetime格式
    print(datetime.datetime.now().ctime())  #Mon Jul  8 09:43:21 2019   str格式
    print(time.ctime())             #Sun Jul  7 23:43:57 2019           str格式

    print(datetime.date.today())    #2019-07-08
    pass

#直接返回当前时间（时间戳）
def nowtime_():
    print(time.time())      #1562514196.39623
    print(datetime.datetime.now().timestamp())  #1562549851.851485
    pass

#当前时间（结构化时间）
def _nowtime():
    print(time.localtime())
    pass

#时间差、时间运算（字符串形式、时间戳形式）
def operation():
    a = datetime.datetime(2019,6,30)
    b = datetime.datetime(2018,5,23)
    now = datetime.datetime.now()
    print(b-a)          #-403 days, 0:00:00
    print("3小时23秒后：",now+datetime.timedelta(hours=3,seconds=23))    #2019-07-08 13:08:24.928534

    c = a + datetime.timedelta(days=1)
    print(c)            #2019-07-01 00:00:00
    d = now - a     #时间相减，返回一个时间间隔对象（timedelta对象）
    print(d,d.days,d.seconds)   #8 days, 10:12:54.147586   8    36774
    pass

#其他形式与时间戳形式相互转换
def transform():
    a = 1562514196.39623    #时间戳
    print(datetime.datetime.fromtimestamp(a))   #2019-07-07 23:43:16.396230     datetime.datetime格式
    print(datetime.date.fromtimestamp(a))       #2019-07-07
    print(time.localtime(a))        #转换为结构化时间，可再进行一次转换，变成str格式
    print(time.ctime(a))                        #Sun Jul  7 23:43:16 2019  (字符串格式)

    b = 'Sun Jul  7 23:43:16 2019'                      #str格式
    c = '2019-07-07 23:41:52.655522'                    #str格式
    d = (2018,12,14,15,15,30,0,0,0)                     #tuple格式
    e = datetime.datetime(2019,6,23,13,23,34,8888)      #datetime.datetime格式
    print(time.mktime(time.strptime(c,'%Y-%m-%d %H:%M:%S.%f')))    #先用time模块转换为结构化格式
    print(datetime.datetime.timestamp(datetime.datetime.strptime(c,'%Y-%m-%d %H:%M:%S.%f')))     #datetime模块先转换为datetime格式
    print(time.mktime(d))                       #1544771730.0
    print(datetime.datetime.timestamp(e))       #1561267414.008888
    pass

#格式化间的转换
def transform_():
    a = '2018/03/04 20:50:00'      #str格式
    b = datetime.datetime(2019,6,23,13,23,34,8888)
    print(datetime.datetime.strptime(a,'%Y/%m/%d %H:%M:%S'))   #2018-03-04 20:50:00  datetime.datetime格式
    print(b.strftime('%Y/%m/%d %H:%M;%S.%f'))   #2019/06/23 13:23:34.008888   str格式
    print(time.strptime(a,'%Y/%m/%d %H:%M:%S'))       #结构化格式<class 'time.struct_time'>
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  #2019-07-08 11:20:55  str格式
    pass

#以指定格式输出
def _week():
    pass

if __name__ == '__main__':
    _week()

"""
返回的时间的格式：
datetime.datetime格式：2019-07-08 14:17:15.176250   #datetime.datetime.now()
datetime.date格式：2019-07-08    #datetime.date.today()
str格式：Mon Jul  8 14:19:33 2019    #datetime.datetime.now().ctime()

str格式：Mon Jul  8 14:22:42 2019    #time.ctime()
结构化格式(time.struct_time)：time.struct_time(tm_year=2019, tm_mon=7, tm_mday=8, tm_hour=14, tm_min=24, tm_sec=42, tm_wday=0, tm_yday=189, tm_isdst=0)   #time.localtime()  

"""















                                      
