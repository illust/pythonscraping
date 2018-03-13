# -*- coding: utf-8 -*-

import scrapy
from xijiSpider.items import xijiSkuSpiderItem

class xijiSkuSpider(scrapy.Spider):

	name = "xijiSkuSpider"

	start_urls = [
			"http://www.xiji.com/product-36171.html"
	]

	def parse(self,response):

		xSpider = xijiSkuSpiderItem()

		url = response.url

		categories = []
		c1 = response.xpath("//div[@class='xj-product-filter-container']/a[3]/text()").extract()[0].strip("\r").strip("\n").strip(" ")
		c2 = response.xpath("//div[@class='xj-product-filter-container']/a[4]/text()").extract()[0].strip("\r").strip("\n").strip(" ")
		c3 = response.xpath("//div[@class='xj-product-filter-container']/a[5]/text()").extract()[0].strip("\r").strip("\n").strip(" ")
		categories.append(c1+"->"+c2+"->"+c3)

		title = response.xpath("//h1/text()").extract()[0].strip("\r").strip("\n").strip(" ")
		subtitle = response.xpath("//div[@class='product-brief-outbox']/div[1]/div[1]/text()").extract()[0].strip("\r").strip("\n").strip(" ")

		xSpider['skuUrl'] = url
		xSpider['skuCtgs'] = categories
		xSpider['skuTitle'] = title
		xSpider['skuSubtitle'] = subtitle

		yield xSpider