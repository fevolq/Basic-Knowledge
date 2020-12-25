#python3.7
#Filename:datetime模块

"""
datetime.date ：表示日期，常用属性：year、month和day
datetime.time ：表示时间，常用属性：hour、minute、second、microsecond
datetime.datetime ：表示日期时间
datetime.timedelta ：表示两个date、time、datetime实例之间的时间间隔，最小可达到微秒
datetime.tzinfo ：时区相关信息对象的抽象基类。由datetime和time类使用，以提供自定义时间而调整。
"""

import datetime

def _date():     #datetime.date类
    #datetime.date(year,month,day)
    from datetime import date
    
    print("最大日期：",date.max)
    print("最小日期：",date.min)

    print("今天的日期：",date.today())
    import time
    print("今天的日期：",date.fromtimestamp(time.time()))     #根据给定的时间戳，返回一个date对象

    now = date.today()
    print("年份：",now.year," 月份：",now.month," 日期：",now.day)
    
    d = date(2018,5,6)
    
    #d.replace(year[,month[,day]])   生成并返回一个新的日期对象，原日期不变
    print(d.replace(2016))
    print(d.replace(2016,3,6))

    #print(d.timetuple())
    print(d.toordinal())    #返回日期是自0001-01-01开始的第多少天
    print(d.weekday())      #返回日期是星期几，[0,6]，0代表星期一
    print(d.isoweekday())   #返回日期是星期几，[1,7]，1代表星期一
    print(d.isocalendar())  #返回一个元组，格式为：(年份，今年的第几个星期，星期几[1,7])

    print(d.isoformat())            #2019-07-07
    print(d.ctime())                #Sun Jul  7 00:00:00 2019
    print(d.strftime('%Y/%m/%d'))    #2019/07/07



def _time():    #datetime.time类
    #datetime.time(hour,[minute,[second,[microsecond,[tzinfo]]]])
    #hour为必须参数，其他为可选参数
    from datetime import time
    
    print("最大时间：",time.max)
    print("最小时间：",time.min)

    t = time(20,5,40,8888)
    print("小时：",t.hour," 分钟：",t.minute," 秒数：",t.second," 微秒：",t.microsecond)

    #t.replace(hour[,minute[,second[,microsecond[,tzinfo]]]])  生成并返回一个新的时间对象，原时间不变
    print(t.replace(21))    

    print(t.isoformat())    #返回一个“HH:MM:SS.%F”格式的时间字符串
    print(t.strftime('%H-%M-%S.%f'))      #返回指定格式的时间字符串


   
def _datetime():    #datetime.datetime类
    #datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    #year、month、day是必须参数
    from datetime import datetime,timezone

    print("现在的时间：",datetime.today())    #返回一个表示当前日期时间的datetime对象
    print("现在的时间：",datetime.now())
    print("某个时区现在的时间："),datetime.now(timezone.utc)
    #datetime.now([tz]  返回指定时区的datetime对象，若不指定tz参数则结果同上
    #datetime.utcnow()  返回当前utc日期时间的datetime对象

    import time
    print(datetime.fromtimestamp(time.time()))      #根据指定的时间戳创建一个datetime对象
    print(datetime.utcfromtimestamp(time.time()))
    print(datetime.strptime('2016/03/04 20:50','%Y/%m/%d %H:%M'))   #将时间字符串转换为datetime对象

    #print(datetime.combine(date(2016,3,4),time(20,50))     #把指定的date和time对象整合成一个datetime对象
    """
    >>> from datetime import date,time,datetime
    >>> datetime.combine(date(2016,3,4),time(20,50))
    datetime.datetime(2016, 3, 4, 20, 50)

    """

    dt = datetime.now()
    print("年份：",dt.year," 月份：",dt.month," 日期：",dt.day," 小时：",dt.hour," 分钟：",dt.minute," 秒数：",dt.second)
    print("时间戳：",dt.timestamp())
    print("date对象：",dt.date()," time对象：",dt.time())

    print(dt.weekday())     #返回星期几，[0,6]
    print(dt.ctime())       #Sun Jul  7 23:43:57 2019
    print(dt.strftime('%Y/%m/%d %H-%M-%S.%f'))      #返回指定格式的时间字符串
    #dt.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])



def _timedelta():   #timedelta类
    #datetime.timedelta(days=0,  seconds=0, microseconds=0, milliseconds=0,  hours=0,  weeks=0)
    #都是默认参数，所以可选，可为整数或浮点数，正数或负数
    #要注意不同单位之间的转换。（如：1小时转换为3600秒）
    from datetime import timedelta

    print(timedelta.max)
    print(timedelta.min)
    print("一年包含的总秒数：",timedelta(365).total_seconds())

    dt = datetime.datetime.now()     #当前时间
    print(dt)
    print("3天后：",dt+datetime.timedelta(3))
    print("3天前：",dt+datetime.timedelta(-3))
    print("3小时后：",dt+datetime.timedelta(hours=3))
    print("3小时30秒后：",dt+datetime.timedelta(hours=3,seconds=30))
    

from datetime import *
def other():    #同类型对象进行比较
    #date2 = date1 + timedelta
    now = date.today()
    print(now)
    tomorrow = now + timedelta(days=1)
    print(tomorrow)

    #timedelta = date1 - date2   两个日期相减，返回一个时间间隔对象
    delta = tomorrow - now
    delta1 = now - tomorrow
    print(delta,'\n',delta1)
    print("两个时间相差{}天".format(delta.days))

    #date1 < date2   两个日期进行比较
    if now < tomorrow:
        print("tomorrow较后")
    else:
        print("now较后")
    
    
if __name__ == '__main__':
    other()





















    
