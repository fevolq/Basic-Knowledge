#!/usr/bin/python3.7
#Filename:根据日期判断是第几天.py

#输入日期，判断这一天是一年的第几天？
'''
class a:
    """
    将小于当月的月份日期累加再加上当月的日期即可得到结果
    """
    print("例a：")
    while True:
        x = int(input('请输入月份：'))
        y = int(input('请输入日期：'))
        dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        d = 0

        if x in range(1,13) and y in range(1,1+dic[x]):
            for i in range(1,13):
                if i < x:
                    d = d + dic[i]
                elif i == x:
                    d += y
                else:
                    print('\n这是一年的第%d天'%d)
                    break
            break      
        else:
            print('\n错误，请重新输入\n')

print("\n")
'''
#import datetime
class b:
    print("例b")
    import datetime
    
    def dayW():
        day = int(input("请输入日期："))
        month = int(input("请输入月份："))
        year = int(input("请输入年份："))
        date1 = datetime.date(year,month,day)
        date2 = datetime.date(year,month=1,day=1)
        return (date1-date2).days + 1

    print(dayW())

print('\nDone')
