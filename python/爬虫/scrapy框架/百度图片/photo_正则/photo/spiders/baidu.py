# -*- coding: utf-8 -*-
import scrapy,re
from photo.items import PhotoItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E4%B8%87%E8%8C%9C&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E4%B8%87%E8%8C%9C&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=star&pn={}&rn=30&gsm={}&1559478136993='
    i = 1
    start_urls = [url.format(i*30,hex(i*30)[2:])]
    
    def parse(self, response):
        src_re = re.compile(r'"thumbURL":"(.*?)"')
        src_list = re.findall(src_re,response.text)
        """
        for src in src_list:
            srcs = []
            item = PhotoItem()
            item['src'] = srcs.append(src)
            yield item
        """
        item = PhotoItem()
        item['src'] = src_list
        yield item
        
        if self.i<1:   
            self.i = self.i + 1
            yield scrapy.Request(self.url.format(i*30,hex(i*30)[2:]),callback = self.parse)

