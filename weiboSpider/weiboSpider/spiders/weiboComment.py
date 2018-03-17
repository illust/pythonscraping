# -*- coding: utf-8 -*-
import scrapy
import re
# import requests
# from scrapy import Selector


class weiboComment(scrapy.Spider):

	name = 'weiboComment'
	allowed_domains = ['weibo.com']
	start_urls = ["https://weibo.com/topgirls8?topnav=1&wvr=6&topsug=1&is_hot=1"]

	def parse(self,response):
		return scrapy.FormRequest.from_response()
		print(response.xpath("//body/div[1]/div[1]/div[4]/div[@class='WB_frame']/").extract_first())