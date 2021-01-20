参考链接：https://b23.tv/z2ReGp

# 创建等

创建项目：scrapy startproject name

进入项目：cd name

进入爬虫文件目录：cd spiders

创建爬虫文件：scrapy genspider 爬虫名name1 “限制的域，即一个网址”。或可直接在对应目录内自创py文件。

运行爬虫：scrapy crawl 爬虫名name1

流程：在items.py内写入字段，需要哪些数据就写多少字段，settings.py内打开需要的管道文件；引擎从爬虫文件内获取第一个start_ur，得到response，交给parse方法处理出需要的数据item或url，item数据交给pipelines.py管道文件处理（保存或者其他），处理完后返回item给引擎，从而得到下一个item，直至最终整个程序运行完。

# 爬虫文件编写

继承于Spider这个父类

name属性是一个标识，爬虫文件名，运行时需要。必不可少

allowed_domains是用于限制爬虫所爬取的域，不在这个域内的网址不进行爬取。可选项

start_urls是起始url，一个可迭代对象，可包含多个url，从前往后，每个url都会执行parse方法。必不可少

parse函数，函数名不可更改。用于从返回的response中提取所需的item和url

需要使用items文件时，需要另外导入items文件内对应的类

回滚新的url：yield scrapy Request(new_url,callback=self.parse)。可定义新的response处理方法parse


# items.py文件

继承于Item类

创建需要的字段：name = scrapy.Field()	类似于字典


# pipelines.py管道文件

处理item数据的文件，可保存本地或存储到数据库。

可写__init__函数进行初始化，整个爬虫运行时只会执行一次

处理item的方法中必须有return item。若有下个class管道类要继续处理item，则传给下个类，否则传给引擎，表示管道已处理完毕，可传入下一个item。若不给引擎返回item，则不会传入新的item数据，程序会卡在这一步。

根据处理不同的数据类型从而继承不同的类，图片和视频有自己的类，然后再重写父类内的方法。


# settings.py配置文件

USER_AGENT最好打开。

ROBOTSTXT_OBEY注释掉或者改为False，否则可能会有的数据无法爬取。

ITEM_PIPELINES需要打开，否则无法执行管道文件。数据在0到1000之间，越小的优先级越高。按此顺序执行对应的管道类。