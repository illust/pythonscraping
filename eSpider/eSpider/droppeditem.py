from collections import defaultdict
from twisted.internet import reactor
from scrapy import signals

class DroppedItemCloseSpider(object):

    def __init__(self, crawler):
        self.crawler = crawler

        self.close_on = {
            'droppeditemcount': crawler.settings.getint('CLOSESPIDER_DROPPEDITEMCOUNT'),
            }

        self.counter = defaultdict(int)

        if self.close_on.get('droppeditemcount'):
            crawler.signals.connect(self.item_dropped, signal=signals.item_dropped)
        crawler.signals.connect(self.spider_closed, signal=signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def item_dropped(self, item, spider):
        self.counter['droppeditemcount'] += 1
        if self.counter['droppeditemcount'] == self.close_on['droppeditemcount']:
            self.crawler.engine.close_spider(spider, 'closespider_droppeditemcount')

    def spider_closed(self, spider):
        task = getattr(self, 'task', False)
        if task and task.active():
            task.cancel()