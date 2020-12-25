#python3.7
#Filename:查询时的防注入问题.py

#此程序不要运行

import pymysql

config = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"mysql",
    "database":"pymysql"
    }
db = pymysql.connect(**config)
cursor = db.cursor()

def search():
    a = "abc' or '123' --"
    b = "qwe"
    sql_1 = "select*from pytest where a='%s' and b='%s'"%(a,b)
    #sql_1 = select*from pytest where a='abc' or '123' -- ' and b='qwe'
    cursor.execute(sql)
    results = cursor.fetchall()
    #mysql中--表示注释，所以这种情况会造成where的条件永远为真

    sql_2 = "select*from pytest where a='%s' and b='%s'"
    cursor.executemany(sql,[('qwe','asd'),("abc' or '123' --","123")])
    #这种情况下，表示执行这个sql语句，元组内的数据是用作查询条件
    #内部执行时，会对查询条件的特殊字符进行\转义
