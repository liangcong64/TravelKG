# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class BaipinitemSpider(scrapy.Spider):
    name = 'baipinItem'
    allowed_domains = ['zhaopin.baidu.com']
    start_urls = ["https://zhaopin.baidu.com/api/qzasync?query=%E6%B1%A0%E5%B7%9E%E6%8B%9B%E8%81%98"
                  "&city=%25E6%25B1%25A0%25E5%25B7%259E&is_adq=1&pcmod=1"
                  "&token=%3D%3DwmnK7qS%2BqoImlYkdpZWi2mopJaHq1kfCHloRJaViGl&pn=0&rn=0"]
    # headers = {'Referer':'https://zhaopin.baidu.com/quanzhi?query=%E6%B1%A0%E5%B7%9E%E6%8B%9B%E8%81%98'
    #                              '&city_sug=%E6%B1%A0%E5%B7%9E'}
    def start_requests(self):
        url = "https://zhaopin.baidu.com/api/qzasync?query=%E6%B1%A0%E5%B7%9E%E6%8B%9B%E8%81%98&city=%25E6%25B1%25A0%25E5%25B7%259E&is_adq=1&pcmod=1&token=%3D%3DwmnK7qS%2BqoImlYkdpZWi2mopJaHq1kfCHloRJaViGl&pn=0&rn=0"
        headers = {'Referer': 'https://zhaopin.baidu.com/quanzhi?query=%E6%B1%A0%E5%B7%9E%E6%8B%9B%E8%81%98'
                                 '&city_sug=%E6%B1%A0%E5%B7%9E'},
        yield Request(url,method='get',headers=headers)
        # return scrapy.FormRequest.from_response(
        #     self.start_urls[0],
        #     headers = {'Referer':'https://zhaopin.baidu.com/quanzhi?query=%E6%B1%A0%E5%B7%9E%E6%8B%9B%E8%81%98'
        #                          '&city_sug=%E6%B1%A0%E5%B7%9E'},
        #
        #     callback = self.parse_response
        # )

    def parse(self,response):
        print(response.text)
