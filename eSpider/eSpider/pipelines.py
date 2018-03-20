# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.exceptions import CloseSpider
# class EspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

class DuplicatesPipeline(object):

	
	def __init__(self):
		self.url_seen = set()

	def process_item(self,item,epet):

		if item['url'] in self.url_seen:
			raise DropItem("Dup item: %s" % item)
		else:
			self.url_seen.add(item['url'])
			return item

	# def process_item(self,item,ctgs):
    #
	# 	if item['url'] in self.url_seenCtg:
	# 		raise DropItem("Duplicate item found: %s" % item)
	# 	else:
	# 		self.url_seenCtg.add(item['url'])
	# 		return item