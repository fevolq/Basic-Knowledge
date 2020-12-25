# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyMysqlPipeline(object):
    def process_item(self, item, spider):
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.db = None
        self.cursor = None

    def process_item(self,item,spider):
        #连接数据库
        self.db = pymysql.connect(host='localhost',user='root',password='mysql',db='scrapy')
        self.cursor = self.db.cursor()

        data = {'src':item['src']}
        
        insert_sql = "insert into test(src) values(%s)"
        try:
            self.cursor.execute(insert_sql,data['src'])
            self.db.commit()
        except Exception as e:
            print('数据问题跳过',e)
            self.db.rollback()
        self.cursor.close()
        self.db.close()
        return item
