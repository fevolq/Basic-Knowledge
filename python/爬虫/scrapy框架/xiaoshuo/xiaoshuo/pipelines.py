# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#保存的方式或数据文件处理的方式
class XiaoshuoPipeline(object):
    def process_item(self, item, spider):
        with open("排名.txt",'a') as f:
            f.write("书名：")
            f.write(item['name'])
            #f.write(item['li'])
            f.write("   作者：")
            f.write(item['author']+'\n')
        return item     #返回item，告诉引擎，已经处理好了，可以进行下一个item数据的提取了
