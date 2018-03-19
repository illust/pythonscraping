# -*- coding: utf-8 -*-
import scrapy
import re


class epetCtgSpider(scrapy.Spider):

    name = 'ctgs'
    allow_domains = ['epet.com']

    # 从命令行输入url
    def __init__(self,*args,**kwargs):
        super(epetCtgSpider,self).__init__(*args,**kwargs)
        self.start_urls = [kwargs.get('start_urls')]
    
    def parse(self,response):

        urlLists = response.xpath("//a[@class='gtitle']//@href").extract()

        for url in urlLists:        # 遍历商品列表
            #title = g.xpath("//div[1]/a[@class='gtitle']/@title").extract_first()
            # url = g.xpath("//div[1]/div[1]/a[@class='gtitle']/@href[1]").extract_first()

            yield scrapy.Request(url=url,callback=self.parse_sku)

        nxtpgUrl = response.xpath("//body/div[3]/div[3]/div[@class='pages']/a[text()='下一页']/@href").extract_first() # 下一页
        if nxtpgUrl is not None:
            yield scrapy.Request(url=nxtpgUrl,callback=self.parse)

    def parse_sku(self,response):

        item = {}

        title = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/h1[@id='abcde']/text()").extract()[0].strip("\n").strip(" ")
        subtitle = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/div[@class='ft14 mt c93c']/text()").extract()[0]
        categories = []
        ctg1 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[1]/span/text()").extract()
        ctg2 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[2]/span/text()").extract()
        ctg3 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[3]/span/text()").extract()
        categories.append(ctg1[0]+"->"+ctg2[0]+"->"+ctg3[0].strip("\r").strip("\n").strip(" "))
        price = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/div[2]/div[2]/span[@id='goods-sale-price']/text()").extract_first()
        
        if title == None:
            item['title'] = None
        else:
            item['title'] = title
        item['subtitle'] = subtitle
        item['url'] = response.url
        item['categories'] = categories
        item['price'] = price

        yield item

            
            