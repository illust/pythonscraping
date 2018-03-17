# -*- coding: utf-8 -*-
import scrapy
import re
#from scrapy.exceptions import CloseSpider
import requests
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
			
			url = link.xpath("./@href").extract_first()
			if url == None:
				pass  
			else:
				_link = re.compile(r'http:[^\s]+list.epet.com/[^\s]+').match(url)

				if _link:
					item = {}
					
					text = link.xpath(".//text()").extract_first()

					res = requests.get(_link[0])
					flg = Selector(res).xpath("//body/div[3]/div[3]/div[@class='bgwhite']/@class").extract_first()
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




