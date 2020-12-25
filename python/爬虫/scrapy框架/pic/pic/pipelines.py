# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class PicPipeline(object):
    def process_item(self, item, spider):
        return item


class DownPipeline(ImagesPipeline):
    def get_request(self,item,info):
        for img_src in item['src']:
            yield scrapy.Request(img_src)
    """
    def file(self,request,response=None,info=None):
        item =  request.meta['item']
        name = item['title']
        return '{}.jpg'.format(name)

    def item_completed(self,results,item,info):
        print(result)
        return item
    """
