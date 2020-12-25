#python3.7
#Filename:mongodb的增删查改（简单版）.py

#先连接mongodb，再连接要用的数据库，最后还需要授权

import pymongo
from pymongo import MongoClient

#连接mongo
mongo_connect = MongoClient(host='localhost',port=27017)

#连接数据库
db = mongo_connect['test']      #连接test数据库

#授权（非常重要，不然会出错）
db.authenticate(name='python',password='python',source='admin')
#name：用户名   password：密码   source：授权数据库

#连接集合
collection = db['text01']       #连接test库里的text01集合

def search():
    """查找"""
    print("\n查找")
    result = collection.find()  #没有pretty()方法
    for i in result:
        print(i)
    return

def update():
    """更新"""
    print("\n更新")
    result = collection.update_one({"name":"fuq"},{"$set":{"age":24,"word":100}})
    print(result)
    print(type(result))
    return

def insert():
    """增加"""
    print("\n增加")
    result = collection.insert_one({"name":"qiang","age":"30"})
    print(result)
    return

def remove():
    """删除"""
    print("\n删除")
    result = collection.delete_one({"name":"qiang"})    #只有delete_one
    print(result)
    return

def agg():
    """聚合"""
    print("\n聚合")
    result = collection.aggregate([{"$group":{"_id":"$age","count":{"$sum":1}}}])
    #通过字段age进行分组，并计算age字段相同值的总和（即每组的数量）
    for i in result:
        print(i)
    return

def main():
    search()
    update()
    search()
    remove()
    search()
    agg()
    search()

if __name__ == '__main__':
    main()
    mongo_connect.close()
    print("\nDone")


"""
注：1.授权操作
    2.mongodb中的执行语句，其中字符串都要加引号
    3.查询操作没有pretty()方法
    4.增加一个文档的操作是“insert_one”，删除一条的操作是“delete_one”。不能略去one，多条则是many
    5.只有查询操作和管道操作才能显示出数据，增改删的返回值都是操作结果的类型。
"""




