# -*- coding: utf-8 -*-
import scrapy
from Job.items import chizhoujobUrl

class ChizhoujoburlSpider(scrapy.Spider):
    name = 'chizhoujobUrl'
    allowed_domains = ['www.chizhoujob.com']
    start_urls = []
    for i in range(20):
        cur = "http://www.chizhoujob.com/job/?Styleid=2&PageNo="+str(i)
        start_urls.append(cur)

    def parse(self, response):
        item_list = response.xpath("//div[@class='seaList']/ul")
        for i_item in item_list:
            jname = i_item.xpath(".//li[@class='li11']//a/text()").extract_first()
            url = i_item.xpath(".//li[@class='li11']//a/@href").extract_first()
            company = i_item.xpath(".//li[@class='li13']//a/text()").extract_first()
            chizhoujoburl = chizhoujobUrl()
            chizhoujoburl['company'] = company
            chizhoujoburl['url'] = url
            chizhoujoburl['jname'] = jname
            yield chizhoujoburl