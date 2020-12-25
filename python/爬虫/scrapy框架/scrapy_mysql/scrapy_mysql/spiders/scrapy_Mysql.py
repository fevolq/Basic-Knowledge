# -*- coding: utf-8 -*-
import scrapy,re
from scrapy_mysql.items import ScrapyMysqlItem

class ScrapyMysqlSpider(scrapy.Spider):
    name = 'scrapy_Mysql'
    allowed_domains = ['menworld.org']
    start_urls = ['https://www.menworld.org/fsbk/']

    def parse(self, response):
        s_re = re.compile(r'img class="lazy" src="(.*?)"')
        se = re.findall(s_re,response.text)
        item = ScrapyMysqlItem()
        for i in se:
            #item['title'] = i[0]
            #srcs = []
            #srcs.append(i)
            item['src'] = i
            yield item
