# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class Test1Middleware(object):




    def process_request(self, request, spider):
        print(11111)
        return None

    def process_response(self, request, response, spider):

        return response
class Test2Middleware(object):




    def process_request(self, request, spider):
        print(2222)
        return None

    def process_response(self, request, response, spider):

        return response

