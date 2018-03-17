# -*- coding: utf-8 -*-

from collections import defaultdict
from twisted.internet import reactor
from scrapy import signals
from scrapy.exceptions import NotConfigured
import logging

logger = logging.getLogger(__name__)

class CloseSpider(object):

    def __init__(self, crawler):
        self.crawler = crawler
        self.item_count = item_count
        self.counter = 0

    @classmethod
    def from_crawler(cls, crawler):
        # first check if the extension should be enabled and raise
        # NotConfigured otherwise
        if not crawler.settings.getbool('MYEXT_ENABLED'):
            raise NotConfigured

        # get the number of items from settings
        item_count = crawler.settings.getint('ITEM_COUNT')

        crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)
        ext = cls(item_count)
        return ext

    def item_scraped(self,item,spider):
        self.counter += 1
        if self.counter == self.item_count:
            logger.info("scraped %d items",self.counter)


    # def drop_item_count(self, item, response, exception, spider):
    #     self.counter['drop_item_count'] += 1
    #     if self.counter['drop_item_count'] == self.close_on['drop_item_count']:
    #         self.crawler.engine.close_spider(spider, 'closespider_drop_item_count')
    #
    # def spider_closed(self, spider):
    #     task = getattr(self, 'task', False)
    #     if task and task.active():
    #         task.cancel()