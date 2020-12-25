#python3.7
#Filename:test2.py

#移动行指针
"""
cursor.scroll(1,mode='relative')  # 相对当前位置移动
cursor.scroll(2,mode='absolute') # 相对绝对位置移动（即相对于首行移动）
第一个值为移动的行数，整数为向下移动，负数为向上移动，mode指定了是相对当前位置移动，还是相对于首行移动
"""

import pymysql

config = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"mysql",
    "database":"pymysql"
    }
db = pymysql.connect(**config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

def move():
    sql = "select*from test2"
    cursor.execute(sql)
    res = cursor.fetchall()
    print("第一次：",res)
    res = cursor.fetchall()
    print("第二次：",res)

    cursor.scroll(0,mode="absolute")    #相对首行移动了0，就是把行指针移动到了首行
    res = cursor.fetchall()     #第三次获取到的内容
    print("第三次：",res)
    cursor.close()

#上下文管理器（使用with语法）
def w():
    db1 = pymysql.connect(**config)
    with db1.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        sql = "select*from test2"
        cursor.execute(sql)
        res = cursor.fetchone()
        print(res)
        cursor.scroll(2,mode="relative")
        res = cursor.fetchone()
        print(res)
        cursor.close()

if __name__ == "__main__":
    move()
    db.close()
