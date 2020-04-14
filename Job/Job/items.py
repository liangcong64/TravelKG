# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ChizhourenUrl(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()

class ChizhouItem(scrapy.Item):
    company = scrapy.Field()
    # txt = scrapy.Field()
    salary = scrapy.Field()
    jname = scrapy.Field()
    mount = scrapy.Field()
    jtxt = scrapy.Field()

class a51jobUrl(scrapy.Item):
    company = scrapy.Field()
    jname = scrapy.Field()
    url = scrapy.Field()

class a51jobItem(scrapy.Item):
    company = scrapy.Field()
    # txt = scrapy.Field()
    salary = scrapy.Field()
    jname = scrapy.Field()
    # mount = scrapy.Field()
    jtxt = scrapy.Field()

class chizhoujobUrl(scrapy.Item):
    company = scrapy.Field()
    jname = scrapy.Field()
    url = scrapy.Field()

class chizhoujobItem(scrapy.Item):
    company = scrapy.Field()
    jname = scrapy.Field()
    salary = scrapy.Field()
    mount = scrapy.Field()
    address = scrapy.Field()
    jtxt = scrapy.Field()
