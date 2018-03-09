# -*- coding: utf-8 -*-

import scrapy
from epetSpider.items import epetSpiderItem
# from scrapy.spiders import CrawlSpider
# from scrapy.linkextractors import LinkExtractor

class epetSpider(scrapy.Spider):

	name = 'epetSpider'

	start_urls = [
			"http://item.epet.com/105952.html"
	]

	def parse(self,response):


		eSpider = epetSpiderItem()

		url = response.url
		categories = []
		ctg1 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[1]/span/text()").extract()
		ctg2 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[2]/span/text()").extract()
		ctg3 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[3]/span/text()").extract()
		categories.append(ctg1[0]+"->"+ctg2[0]+"->"+ctg3[0].strip("\r").strip("\n").strip(" "))
		title = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/h1[@id='abcde']/text()").extract()[0].strip("\n").strip(" ")
		subtitle = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/div[@class='ft14 mt c93c']/text()").extract()[0]
		price = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/div[2]/div[2]/span[@id='goods-sale-price']/text()").extract_first()
		
		eSpider["skuUrl"] = url
		eSpider["skuCtgs"] = categories	
		eSpider["skuTitle"] = title
		eSpider["skuSubTitle"] = subtitle
		eSpider["skuPrice"] = price 


		yield eSpider