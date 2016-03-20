#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""
from scrapydemo.items import HuxiuItem
import scrapy


class HuxiuSpider(scrapy.Spider):
    name = "huxiu"
    allowed_domains = ["huxiu.com"]
    start_urls = [
        "http://www.huxiu.com/index.php"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="mod-info-flow"]/div/div[@class="mob-ctt"]'):
            print("huxiu link..")
            item = HuxiuItem()
            item['title'] = sel.xpath('//h3/a/text()').extract()
            item['link'] = sel.xpath('//h3/a/@href').extract()
            item['desc'] = sel.xpath('div[@class="mob-sub"]/text()').extract()
            print(item['title'],item['link'],item['desc'])
            yield item
