# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
from scrapy.http import Request

class PhotoPipeline(object):
    def process_item(self, item, spider):
        return item


class DownPipeline(ImagesPipeline):
    #IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
    
    def get_request(self,item,info):
        yield scrapy.Request(url=item['src'])
    """
    def file_path(self,request,response=None,info=None):
        item = request.meta['item']
        image_name = item['src'][0].split('/')[-1]
        return '%s.jpg'%image_name

    def item_completed(self,results,item,info):
        print(results)
        return item
    """
