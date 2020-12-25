#python3.7
#Filename:插入多条数据.py

#使用pymysql库内的test1表

import pymysql

config = {
    "host":"127.0.0.1",
    "user":"root",
    "password":"mysql",
    "database":"pymysql"
    }
db = pymysql.connect(**config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
#默认情况返回的是元组，只能看到每行的数据，却不知道每一列代表的是什么，这个时候可以使用以下方式来返回字典，每一行的数据都会生成一个字典：
#在实例化的时候，将属性cursor设置为pymysql.cursors.DictCursor

def search():
    sql_search = "select*from test"
    try:
        cursor.execute(sql_search)
        results = cursor.fetchall()
        print("name","pass")

        for row in results:
            print(row)
            #name = row[0]
            #password = row[1]
            #print(name,password)
        print("\n")

    except Exception as e:
        raise e    

#插入多条数据
def insert_many():
    sql_insert = "insert into test1(name,pass) VALUES(%s,%s)"
    cursor.executemany(sql_insert,[("tom","456"),("jack","654")])  #插入多条数据
    db.commit()

def res():
    sql = "delete from test1 where name=%s"     #删除数据
    res = cursor.executemany(sql,("tom",))  #execute()和executemany()都会返回受到的影响的行数
    print("response=",res)   #返回受影响的行数

def main():
    search()
    insert_many()
    search()
    res()
    search()
    cursor.close()
    db.close()
    print("Done")

if __name__ == "__main__":
    main()
    print("Done")

"""
当表中有自增主键时，可使用lastrowid来获取最后一次自增id。
print("最后一次自增是：",cursor.lastrowid)
"""
