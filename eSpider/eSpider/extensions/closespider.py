# -*- coding: utf-8 -*-

from collections import defaultdict
from twisted.internet import reactor
from scrapy import signals

class CloseSpider(object):

    def __init__(self, crawler):
        self.crawler = crawler

        self.close_on = {
            'drop_item_count': crawler.settings.getint('CLOSESPIDER_DROP_ITEM_COUNT'),
        }

        self.counter = defaultdict(int)

        if self.close_on.get('drop_item_count'):
            crawler.signals.connect(self.drop_item_count, signal=signals.item_dropped)

        crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def drop_item_count(self, item, response, exception, spider):
        self.counter['drop_item_count'] += 1
        if self.counter['drop_item_count'] == self.close_on['drop_item_count']:
            self.crawler.engine.close_spider(spider, 'closespider_drop_item_count')

    def spider_closed(self, spider):
        task = getattr(self, 'task', False)
        if task and task.active():
            task.cancel()