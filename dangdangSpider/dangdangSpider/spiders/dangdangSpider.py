# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from dangdangSpider.items import dangdangSpiderItem
from bs4 import BeautifulSoup


class Spider(CrawlSpider):

	name = 'dangdangSpider'

	allowed_domains = ['dangdang.com']

	start_urls = [
			"http://product.dangdang.com/24031944.html"
	]

	def parse_sku(self,response):
		skuItem = dangdangSpiderItem()
		# soup = BeautifulSoup(response.text,"html.parser")
		# skuItem['sku_title'] = soup.find("h1").get("title") # 单品名称
		# skuItem['sku_price'] = soup.find("div",class_="price_d").get_text()[4:].strip("\n") # 单品价格

		# # 单品相关信息
		# skuDtls = [] 
		# skuDetails = soup.find_all("div",class_="pro_content",id="detail_describe")[0].find("ul",class_="key clearfix")
		# for item in skuDetails.find_all("li"):
		# 	skuDtls.append(item.get_text())
		# skuItem['sku_other_info'] = skuDtls
		skuItem['sku_title'] = response.css('title').extract_first()


