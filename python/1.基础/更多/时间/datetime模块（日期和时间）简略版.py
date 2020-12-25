#!/usr/bin/python3.7
#Filename:datetime模块（日期和时间）.py

#内置的datetime模块支持日期和时间的算法（注意内部关键字的大小写的不同用法）

class a1:
    from datetime import date
    now = date.today()      #返回现在的时间（年份-月份-日期）
    print(now)
    now_1 = now.strftime("%m-%d-%y. %d %B %Y is a %A on the %d day of %B.")
    print(now_1)

print("\n")

class a2:
    import datetime
    print(datetime.date.today())
    print(datetime.date.today().strftime("月份-日期-年份：%m-%d-%y。\
“日期转换为哪个月的第几天，是星期几”：%d %b %y 是 %a 在 %b 的 %D 天"))

#数字月份%m，数字日期%d，数字年份%Y，英文月份%B，英文星期%A
#年份y小写，则为后两位；月份b小写，则输出月份的缩写；星期a小写，则输出缩写
#日期d小写，则输出几号，大写则输出完整的日期（月份/几号/年份）
#%H 24小时制；%I12小时制；%M 分钟数；%S 秒

print("\n\n")

from datetime import date,timedelta
birthday = date(1995,6,29)
now = date.today()
age = now - birthday
print("他出生了",age.days,"天")         #出生了多少天

print(now - timedelta(1))      #昨天的日期

#时间戳
from datetime import datetime
datetime_stamp = datetime.timestamp(datetime.now())
print('时间戳：',datetime_stamp)
datetime_str = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
print(datetime_str)


print("\nDone")
"""
%a  本地（locale）简化星期名称
%A  本地完整星期名称
%b  本地简化月份名称
%B  本地完整月份名称
%c  本地相应的日期和时间表示
%d  一个月中的第几天（01 - 31）
%H  一天中的第几个小时（24小时制，00 - 23）
%I  第几个小时（12小时制，01 - 12）
%j  一年中的第几天（001 - 366）
%m  月份（01 - 12）
%M  分钟数（00 - 59）
%p  本地am或者pm的相应符
%S  秒（01 - 61）
%U  一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。
%w  一个星期中的第几天（0 - 6，0是星期天）
%W  和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x  本地相应日期
%X  本地相应时间
%y  去掉世纪的年份（00 - 99）
%Y  完整的年份
%Z  时区的名字（如果不存在为空字符）
%%  ‘%’字符
"""
