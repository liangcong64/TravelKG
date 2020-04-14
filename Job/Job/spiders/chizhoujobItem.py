# -*- coding: utf-8 -*-
import scrapy
import csv
from Job.items import chizhoujobItem

class ChizhoujobitemSpider(scrapy.Spider):
    name = 'chizhoujobItem'
    allowed_domains = ['www.chizhoujob.com']
    start_urls = []
    file_object = csv.reader(open('data/chizhou/chizhoujobUrl.csv', 'r', encoding='utf-8'))
    for wordList in file_object:  ##生成url列表
        str = wordList[2]
        cur = "http://www.chizhoujob.com"+str
        start_urls.append(cur)

    def parse(self, response):
        jname = response.xpath("//div[@class='jobname']/text()").extract_first()
        company = response.xpath("//div[@class='names']//p/a/text()").extract_first()
        salary = response.xpath("//div[@class='basic']/ul/li[1]/text()").extract_first()
        mount = response.xpath("//div[@class='basic']/ul/li[5]/text()").extract_first()
        jtxt = response.xpath("//div[@class='basic']/ul/li[3]/text()").extract_first()
        address = response.xpath("//div[@class='basic']/ul/li[4]/i/text()").extract_first()
        chizhoujobitem = chizhoujobItem()
        chizhoujobitem['jname'] = jname
        chizhoujobitem['salary'] = salary
        chizhoujobitem['company'] = company
        chizhoujobitem['mount'] = mount
        chizhoujobitem['jtxt'] = jtxt
        chizhoujobitem['address'] = address
        yield chizhoujobitem