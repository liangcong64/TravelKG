# -*- coding: utf-8 -*-
import scrapy
from Job.items import a51jobUrl

class A51joburlSpider(scrapy.Spider):
    name = '51jobUrl'
    allowed_domains = ['search.51job.com']
    start_urls = []
    for i in range(1,16):
        cur = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%25B1%25A0%25E5%25B7%259E,2,"+str(i)+".html?lang" \
            "=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=" \
            "-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        start_urls.append(cur)

    def parse(self, response):
        item_list = response.xpath("//div[@class='dw_table']//div[@class='el']")
        for i_item in item_list:
            jname = i_item.xpath(".//p/span/a/text()").extract_first().strip()
            company = i_item.xpath(".//span[@class='t2']/a/text()").extract_first()
            url = i_item.xpath(".//p/span/a/@href").extract_first()
            a51joburl = a51jobUrl()
            a51joburl['jname'] = jname
            a51joburl['company'] = company
            a51joburl['url'] = url
            yield a51joburl

