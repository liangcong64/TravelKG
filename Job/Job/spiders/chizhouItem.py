# -*- coding: utf-8 -*-
import scrapy
import csv
from Job.items import ChizhouItem

class ChizhouitemSpider(scrapy.Spider):
    name = 'chizhouItem'
    allowed_domains = ['job.chizhouren.com']
    start_urls = []
    # file_object = csv.reader(open('data/chizhou/zhaopinurl1.csv', 'r', encoding='utf-8'))
    # for wordList in file_object:  ##生成url列表
    #     str = wordList[2][9:-5]
    #     cur = "http://job.chizhouren.com/company/jobs/"+str+"-.html"
    #     start_urls.append(cur)

    def parse(self, response):
        company = response.xpath("//div[@class='cname']/text()").extract_first().strip()
        # txt = response.xpath("//div[@class='cominfo']/div[@class='txt']/text()").extract_first()
        item_list = response.xpath("//div[@class='jobslist J_jobsList']")
        for i_item in item_list:
            jname = i_item.xpath(".//div[@class='jname']/a/strong/text()").extract_first()
            mount = i_item.xpath("./div[@class='jname']/span[1]/text()").extract_first()
            jtxt = i_item.xpath(".//div[@class='jtxt']/text()").extract()
            salary = i_item.xpath(".//div[@class='jtxt']/u/text()").extract_first()
            chizhouItem = ChizhouItem()
            chizhouItem['company'] = company
            chizhouItem['jname'] = jname
            chizhouItem['mount'] = mount
            chizhouItem['jtxt'] = jtxt
            chizhouItem['salary'] = salary
            yield chizhouItem
