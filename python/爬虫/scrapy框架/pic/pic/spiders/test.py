# -*- coding: utf-8 -*-
import scrapy,re
from pic.items import PicItem

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['menworld.org']
    start_urls = ['https://www.menworld.org/fsbk/']

    def parse(self, response):
        s_re = re.compile(r'img class="lazy" src="(.*?)"')
        se = re.findall(s_re,response.text)
        item = PicItem()
        srcs = []
        for i in se:
            #item['title'] = i[0]
            srcs.append(i)
        item['src'] = se
        yield item

#先在网址中找出图片的地址，存放到一个列表中，再用生成器调用这个图片地址列表
