# -*- coding: utf-8 -*-
import scrapy
import re


class epetCtgSpider(scrapy.Spider):

	name = 'ctgs'
	allow_domains = ['epet.com']

	start_urls = ['http://list.epet.com/7e3543.html',]
	
	def parse(self,response):

		glists = response.xpath("//body/div[3]/div[3]/div[3]//div[@class='list_box-li']")

		for g in glists:		# 遍历商品列表
			#title = g.xpath("//div[1]/a[@class='gtitle']/@title").extract_first()
			url = g.xpath("//div[1]/div[1]/a[@class='gtitle']/@href[1]").extract_first()

			yield scrapy.Request(url=url,callback=self.parse_sku)

		nxtpgUrl = response.xpath("//body/div[3]/div[3]/div[@class='pages']/a[@name]/@href").extract_first() # 下一页
		if nxtpgUrl is not None:
			yield scrapy.Request(url=nxtpgUrl,callback=self.parse)

	def parse_sku(self,response):

		item = {}
		title = response.xpath("//title").extract_first()
		if title == None:
			item['title'] = None
		else:
			item['title'] = title
		item['link'] = response.url
		yield item 

			
			