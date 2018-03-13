# -*- coding: utf-8 -*-


import scrapy
from scrapy import Item,Field

class xijiSkuSpiderItem(Item):
    
    skuUrl = scrapy.Field()     # 商品url
    skuCtgs = scrapy.Field()	# 存储分类信息
    skuTitle = scrapy.Field()	# 商品名称
    skuSubtitle = scrapy.Field()# 商品子标题
    # skuPrice = scrapy.Field()	# 商品价格
    # skuParas = scrapy.Field()	# 商品其他参数
