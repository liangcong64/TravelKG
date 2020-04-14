# -*- coding: utf-8 -*-
import scrapy
import csv
from Job.items import a51jobItem

class A51jobitemSpider(scrapy.Spider):
    name = '51jobItem'
    allowed_domains = ['jobs.51job.com']
    start_urls = []
    file_object = csv.reader(open('data/chizhou/51jobUrl4.csv', 'r', encoding='utf-8'))
    for wordList in file_object:  ##生成url列表
        str = wordList[2]
        print(str)
        start_urls.append(str)

    def parse(self, response):
        company = response.xpath("//p[@class='cname']/a/@title").extract_first().strip()
        jname = response.xpath("//div[@class='cn']/h1/@title").extract_first()
        jtxt = response.xpath("//p[@class='msg ltype']/@title").extract()
        salary = response.xpath("//div[@class='cn']/strong/text()").extract_first()
        a51jobitem = a51jobItem()
        a51jobitem['company'] = company
        a51jobitem['jname'] = jname
        a51jobitem['jtxt'] = jtxt
        a51jobitem['salary'] = salary
        yield a51jobitem
