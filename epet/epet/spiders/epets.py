# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse

class EpetsSpider(CrawlSpider):
    name = 'epets'
    allowed_domains = ['epet.com']
    start_urls = ['http://www.epet.com/']

    rules = (
        Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),
    )

    def parse_item(self, HtmlResponse):

        self.html_file = open('d:\\temp\\'+HtmlResponse.xpath("//title/text()").extract_first()+'.html','w',encoding='utf-8')
        self.html_file.write(HtmlResponse.body.decode("utf-8"))
        self.html_file.close()
