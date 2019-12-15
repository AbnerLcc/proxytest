#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

class Command(ScrapyCommand):
    requires_project = True
    def syntax(self):
        return '[options]'

        # 自定制命令描述,当在终端中输入scrapy -- help时,紧跟crawlall  的解析
    def short_desc(self):
        return 'Runs all of the spiders'

        #  当在终端中输入 scrapy crawlall时,会执行run方法

    def run(self, args, opts):
            #  到setting中获取所有爬虫任务类
            # 自定义下载任务,并强转列表
        spider_list = self.crawler_process.spiders.list()

        for name in spider_list:
            self.crawler_process.crawl(name, **opts.__dict__)

            # 开始爬虫
        print(type(self.crawler_process.spiders.list))
        self.crawler_process.start()
# start=Command()
# start.run()