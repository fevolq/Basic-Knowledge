#python3.7
#Filename:面向对象的mongodb操作.py

#本地没有此程序运行需要的数据库

from pymongo import MongoClient


class MongoUtil(object):

    def __init__(self,host,port,db):
        self.conn = MongoClient(host=host,port=port)    #连接mongo
        self.db = self.conn[db]     #连接数据库

    def get_state(self):
        return True

    def auth(self,name,password,source):    #授权
        '''
        登录
        :param name:用户名
        :param password:密码
        :param source:授权数据库
        :return: true/false
        '''
        if self.get_state():
            try:
                return self.db.authenticate(name=name,password=password,source=source)
            except:
                return False
        else:
            return False

    def insert_one(self,collection,document):
        '''
        插入单条
        :param collection: 集合名
        :param document: 文档（单条），类型：dict
        :return: 插入的这条数据的ID
        '''
        if self.get_state():
            result = self.db[collection].insert_one(document=document)
            return result.inserted_id
        else:
            return ''

    def insert_many(self,collection,documents):
        '''

        :param collection: 集合名
        :param documents: 文档（多条）,类型：list(dict)
        :return: 受影响的ID
        '''
        if self.get_state():
            result = self.db[collection].insert_many(documents=documents)
            return result.inserted_ids
        else:
            return ''

    def update_one(self,collection,filter,update,upsert=False):
        '''

        :param collection:集合名
        :param filter:删选条件
        :param update:dict，更新的内容
        :param upsert:若没有符合该条件的文档，是否新增
        :return:修改后的结果
        '''
        if self.get_state():
            return self.db[collection].update_one(filter=filter,update=update,upsert=upsert)
        else:
            return None

    def update_many(self,collection,filter,update,upsert=False):
        '''

        :param collection:
        :param filter:
        :param update:list(dict)
        :param upsert:
        :return:修改后的结果
        '''
        if self.get_state():
            return  self.db[collection].update_many(filter=filter,update=update,upsert=upsert)
        else:
            return None

    def find(self,collection,filter=None,column=None):
        '''
        :param collection:集合名
        :param filter:过滤器
        :param column:投影
        :return:结果集
        '''
        if self.get_state():
            result = self.db[collection].find(filter,column)
            return result
        else:
            return None

    def  delete_one(self,collection,filter):
        '''
        :param collection:
        :param filter:
        :return:删除的条数
        '''
        if self.get_state():
            return self.db[collection].delete_one(filter=filter)
        else:
            return 0

    def  delete_many(self,collection,filter):
        '''
        :param collection:
        :param filter:
        :return:删除的条数
        '''
        if self.get_state():
            return self.db[collection].delete_many(filter=filter)
        else:
            return 0

    def aggregate(self,collection,pipline):
        '''

        :param collection:
        :param pipline: 管道（如果多个阶段，需要list,例如：[{'$group':...},{'$match':...}]）
        :return:
        '''
        if self.get_state():
            result = self.db[collection].aggregate(pipeline=pipline)
            return result
        else:
            return None

    def close(self):
        self.conn.close()



if __name__ == '__main__':
    # 链接mongo
    mongo = MongoUtil(host='192.168.1.29',port=27017,db='python')
    # 授权
    result = mongo.auth(name='liumingyi',password='123456',source='admin')
    if result:
        # 操作:单条插入
        insertID = mongo.insert_one(collection='car',document={'car':'奥拓','price':3000})
        #输出刚才插入的数据
        result = mongo.find(collection='car',filter={'_id':insertID})
        for i in result:
            print(i)
        # 更新
        # result = mongo.update_one(collection='car',filter={'name':'奥拓5'},update={'$set':{'price':5000}},upsert=True)
        # print(result)
        # result = mongo.update_many(collection='car', filter={'car': '奥拓'}, update={'$set': {'price': 5000}})
        # print(result)

        # 删除
        result = mongo.delete(xxx)

    else:
        print('授权失败')
