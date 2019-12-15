# -*- coding: utf-8 -*-
import scrapy

class ChoutiSpider(scrapy.Spider):
    name = 'chou'
    allowed_domains = ['*']
    start_urls = [ 'https://dig.chouti.com/']
    def parse(self,response):
        pass


