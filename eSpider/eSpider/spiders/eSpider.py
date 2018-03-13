# -*- coding: utf-8 -*-
import scrapy
import re

class eSpider(scrapy.Spider):

	name = 'epet'
	allowed_domains = ['epet.com']
	start_urls = ['http://list.epet.com/3620.html']

	def parse(self,response):

		links = response.xpath("//a")
		for link in links:
			
			url = link.xpath("./@href").extract_first()
			if url == None:
				pass  
			else:
				_link = re.compile(r'(http[s]{0,1}):[^\s]*list.epet.com/[^\s]+.html').match(url)

				if _link:
					item = {}
					item["link_text"] = link.xpath(".//text()").extract_first()
					
					item["link"] = _link[0]

					yield scrapy.Request(url=_link[0],callback=self.parse)

					yield item

