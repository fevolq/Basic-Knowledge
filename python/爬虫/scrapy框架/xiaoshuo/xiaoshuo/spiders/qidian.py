# -*- coding: utf-8 -*-
import scrapy
from xiaoshuo.items import XiaoshuoItem

class QidianSpider(scrapy.Spider):
    name = 'qidian_wanben'      #爬虫文件的唯一名字(不伦是不是在同一个scrapy项目中)，也是运行scrapy时使用的名字
    allowed_domains = ['qidian.com']    #域名，以后要爬取的网址都必须在这个域名下
    start_urls = ['https://www.qidian.com/finish?chanId=22']    #初始网址
    
    def parse(self, response):
        lists = response.xpath('//ul[@class="all-img-list cf"]/li')
        for i in lists:
            item = XiaoshuoItem()       #以字典形式
            #item['li'] = i.xpath('./@data-rid').extract()[0]
            item['name'] = i.xpath('./div[@class="book-mid-info"]/h4/a/text()').extract()[0]
            item['author'] = i.xpath('./div[@class="book-mid-info"]/p[@class="author"]/a[@class="name"]/text()').extract()[0]
            yield item
    """
    def parse(self, response):
        item = XiaoshuoItem()
        item['name'] = '123'
        item['author'] = 'abc'
        yield item
    """
