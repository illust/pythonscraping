# -*- coding: utf-8 -*-
import scrapy
from epetSpider.items import epetMainSpiderItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class EpetmainspiderSpider(CrawlSpider):

    name = 'epetMainSpider'

    def __init__(self):

    	self.urlSet = []
    	self.allowed_domains = ['http://www.epet.com']
    	self.start_urls = ['http://www.epet.com']
    	self.rules = (
    		Rule(LinkExtractor(allow=r'www.epet.com/.*?')),
    		Rule(LinkExtractor(allow=r'list.epet.com/\d+.html'),callback='parse_start_url',follow=True),
    		)

    def start_requests(self):
    	for url in self.start_urls:
    		yield scrapy.Request(url,callback=self.parse,dont_filter=True)


    def parse_start_url(self, response):
        

        sel = scrapy.Selector(response)

        links_in_a_page = sel.xpath('//a[@href]') # 页面内所有链接

        for links_sel in links_in_a_page:

        	item = epetMainSpiderItem()
        	link = str(links_sel.re('href="(.*?)"')[0]) # 每一个url

        	if link:
        		
        		if link.startswith('http') and link.endswith('html'): # 处理相对url
        			if link not in self.urlSet:
        				self.urlSet.append(link)
        				print(link)

        				yield scrapy.Request(link,callback=self.parse_start_url) # 生成新的请求，递归回调self.parse
        				
        				item['link'] = link
        				link_text = links_sel.xpath('text()').extract() # 每个url的链接文本，若不存在设为None
        				if link_text:
        					item['link_text'] = str(link_text[0])
        				else:
        					item['link_text'] = None
        				im = dict(item)
        				print(im)
        				yield item