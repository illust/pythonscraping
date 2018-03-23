# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import CloseSpider

class skuSpider(CrawlSpider):

	name = 'sku'

	settings = get_project_settings()
    allowed_domains = settings.get('ALLOWED_DOMAINS')
    start_urls = settings.get('START_URLS')
    reRule = settings.get('RERULE')

    rules = (
        Rule(LinkExtractor(allow=reRule), callback='parse_item', follow=True),
    )

    def parse_item(self,response):
    	