# -*- coding: utf-8 -*-

import scrapy
from scrapy import Item,Field


class Article(Item):
    
    title = scrapy.Field() 
