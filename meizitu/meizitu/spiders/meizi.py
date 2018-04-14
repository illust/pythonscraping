# -*- coding: utf-8 -*-
import scrapy
from meizitu.items import MeizituItem

class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://meizitu.com/']

    def parse(self, response):
        tagsUrlList = response.xpath("//div[@class='tags']/span/a/@href").extract()
        for tagUrl in tagsUrlList:
            yield scrapy.Request(url=tagUrl,callback=self.parse_tag)

    def parse_tag(self,response):
        catsUrlList = response.xpath("//li[@class='wp-item']/div[1]/div[1]/a/@href").extract()
        for catsUrl in catsUrlList:
            yield scrapy.Request(url=catsUrl,callback=self.parse_item)

    def parse_item(self,response):
        picsList = response.xpath("//div[@id='picture']/p/img/@src").extract()
        for picUrl in picsList:
            item = MeizituItem()
            item['image_urls'] = [picUrl]
            yield item