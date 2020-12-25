#python3.7
#Filename:使用pymysql连接使用mysql.py

#注意用户名、密码、端口号和使用的库、表名

import pymysql

#连接数据库
db = pymysql.connect(host="localhost",user="root",password="mysql",db="pymysql",port=3306,charset="utf8")
#主机名或者主机地址，用户名，密码，db="使用的库名"，port="端口号"，......

cur = db.cursor()   #使用cursor()方法创建一个游标对象

#查询操作
def search():
    sql = "select * from test"      #编写sql语句
    try:
        cur.execute(sql)     #执行sql语句
        results = cur.fetchall()     #获取查询的所有记录
        #fetchone获取下一行数据，第一次为首行，fetchmany(n)获取剩余结果的前n行
        print("id","name")
        #print(results)
        #查询的结果是一个元组元组的格式，每一条数据条是一个元组，多个元组组成显示出的元组结果。
    
        for row in results:
            #print(row)
            id = row[0]
            name = row[1]
            print(id,name)

    except Exception as e:
        raise e

#插入操作
def insert():
    sql_insert = "insert into test(id,name) values(6,'abc')"
    try:
        cur.execute(sql_insert)
        db.commit()     #提交，否则插入的数据不生效（增删改操作都需要提交）
    except Exception as e:
        db.rollback()   #错误回滚

#更新操作
def update():
    sql_update = "update test set name = '%s' where id = %d"
    try:
        cur.execute(sql_update % ("qwe",6))
        db.commit()
    except Exception as e:
        db.rollback()
    
#删除操作
def delete():
    sql_delete = "delete from test where id = %d"
    try:
        cur.execute(sql_delete%(6))
        db.commit()
    except Exception as e:
        db.rollback()

def main():
    search()        #查
    print("\n")
    insert()        #增
    search()
    print("\n")
    update()        #改
    search()
    print("\n")
    delete()        #删
    search()
    print("\n")

    db.close()
    

if __name__ == "__main__":
    #main()
    search()
    print("\nDone")

"""
import mysql.connector    #内置的模块

db = mysql.connector.connect(user='root',passwd='root',database='test')
cursor = db.cursor()
"""
