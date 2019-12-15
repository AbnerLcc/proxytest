# -*- coding: utf-8 -*-
import scrapy

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['*']
    start_urls = [ 'https://dig.chouti.com/']
    cookie_dict = {}
    def parse(self,response):
        print(response)


