# -*- coding: utf-8 -*-
import scrapy
from Job.items import ChizhourenUrl


class ChizhouurlSpider(scrapy.Spider):
    name = 'chizhouurl'
    allowed_domains = ['job.chizhouren.com']
    start_urls = []
    for i in range(50):
        cur = 'http://job.chizhouren.com/jobs/jobs_list/page/'+str(i)+'.html'
        start_urls.append(cur)

    def parse(self, response):
        item_list = response.xpath("//div[@class='J_jobsList yli']")
        for i_item in item_list:
            name = i_item.xpath(".//a[@class='line_substring']/text()").extract_first()
            url = i_item.xpath(".//a[@class='line_substring']/@href").extract_first()
            chizhouren = ChizhourenUrl()
            chizhouren['name'] = name
            chizhouren['url'] = url
            yield chizhouren