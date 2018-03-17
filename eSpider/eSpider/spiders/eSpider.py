# -*- coding: utf-8 -*-
import scrapy
import re
#from scrapy.exceptions import CloseSpider
#import requests
from scrapy import Selector

class eSpider(scrapy.Spider):

	name = 'epet'
	allowed_domains = ['epet.com']
	start_urls = ['http://www.epet.com']
	# def __init__(self):
	# 	self.count = 0 # 设置初始个数
	# 	self.max_count = 20 # 设置最大个数


	def parse(self,response):

		links = response.xpath("//a")
		for link in links:

			# 提取url
			url = link.xpath("./@href").extract_first()
			if url == None:
				pass  
			else:
				_link = re.compile(r'http:[^\s]+list.epet.com/[^(search)][^\s]+').match(url) # 利用正则表达式匹配 list.epet.com
				# 如果url匹配到，则进行相应操作
				if _link:
					item = {}
					# 获得链接内部文本
					text = link.xpath(".//text()").extract_first()
					# 重新发起一个请求，查看该list页面是否为空（不含任何商品）
					# res = requests.get(_link[0])
					# flg = Selector(res).xpath("//body/div[3]/div[3]/div[@class='bgwhite']/@class").extract_first()
					# 如果为空，则该分类目录下无商品，视为无效，否则保存链接，继续其他操作
					flg = 'contents'
					if flg == 'bgwhite':
						pass
					else:
						if text == None:
							item["link_text"] = None
						else:
							item["link_text"] = text.strip(" ").strip("\n")
						item["link"] = _link[0]
					
						yield scrapy.Request(url=_link[0],callback=self.parse)
	
						yield item
					# self.count = self.count + 1
					# if self.count == self.max_count:
					# 	raise CloseSpider('The number of extracted data is enough!')




