# -*- coding: utf-8 -*-

import scrapy
from scrapy import Field,Item

class epetSpiderItem(Item):
    
    skuUrl = scrapy.Field()     # 商品url
    skuCtgs = scrapy.Field()	# 存储分类信息
    skuTitle = scrapy.Field()	# 商品名称
    skuSubTitle = scrapy.Field()# 商品子标题
    skuPrice = scrapy.Field()	# 商品价格
    # skuParas = scrapy.Field()	# 商品其他参数

class epetMainSpiderItem(Item):

	link = scrapy.Field()
	link_text = scrapy.Field()

