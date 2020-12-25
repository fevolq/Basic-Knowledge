import time

#时间戳：距离1970年01月01日00:00:00多少秒。
print("时间戳：",time.time())  #返回当前时间的时间戳

print("结构化：",time.localtime())     #结构化时间对象
print(time.gmtime())        #与上面只相差8个小时

tl = time.localtime()
print(tl.tm_year)   #拆分取出结构化时间的某项


print('\n')
#时间的转换
print(time.localtime(1562479026))   #将指定时间戳转换为结构化时间
print(time.strptime('2018-03-04','%Y-%m-%d'))   #将指定字符串时间转换为结构化时间


t = (2018,12,14,15,15,30,0,0,0)     
print(time.mktime(t))   #将指定时间转换为时间戳
print(time.mktime(time.localtime()))    #将当前时间的结构化时间转换为时间戳
print(time.strftime("%Y-%m-%d",time.localtime()))   #将当前时间的结构化时间转换为字符串时间

print(time.strftime('%y/%m/%d %H:%M:%S'))   #（不传入结构化时间，则）以指定格式返回当前时间的字符串


print('\n')
#time.ctime(时间戳)    如果不传入参数，则直接返回当前时间的格式化字符串
print(time.ctime())     #Sun Jul  7 22:59:51 2019
print(time.ctime(1562511600))


time.sleep(1)   #（程序运行）延迟1秒
