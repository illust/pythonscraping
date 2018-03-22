# -*- coding: utf-8 -*-
import scrapy
import re

class epetSpider(scrapy.Spider):

	name = 'epet'
	allowed_domains = ['epet.com']
	start_urls = ['http://www.epet.com/']

	def parse(self,response):

		links = response.xpath("//a")
		# linklst = []
		i = 0
		for link in links:
			

			url = link.xpath("./@href").extract_first()
			if url == None:
				return 

			_link = re.compile(r'(http[s]{0,1}):[^\s]*epet.com[^\s]*').match(url)

			if _link:
				item = {}
				item["link_text"] = link.xpath(".//text()").extract_first()
					
				item["link"] = _link[0]

				i = i + 1
				print(i)
				print(_link[0])

				yield scrapy.Request(url=_link[0],callback=self.parse)

				yield item

