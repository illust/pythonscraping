# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import CloseSpider
import json
import re

class skuSpider(CrawlSpider):

    name = 'sku'
    settings = get_project_settings()
    allowed_domains = settings.get('ALLOWED_DOMAINS')
    start_urls = settings.get('START_URLS')
    reRule = settings.get('RERULE')

    global pageRule
    pageRule = settings.get('PAGERULE')

    custom_settings = {
        'DEPTH_PRIORITY':1,
        'SCHEDULER_DISK_QUEUE':'scrapy.squeue.PickleFifoDiskQueue',
        'SCHEDULER_MEMORY_QUEUE':'scrapy.squeue.FifoMemoryQueue'
        }

    rules = (
        Rule(LinkExtractor(allow=reRule), callback='parse_sku', follow=True),
    )

    # def parse_item(self,reponse):
    #     links = reponse.xpath("//a")
    #     for link in links:
    #         # 提取url 
    #         lnk = link.xpath("./@href").extract_first()
    #         if lnk == None:
    #             pass 
    #         else:
    #             url = re.compile(pageRule).match(lnk) # 利用正则表达式匹配符合规则的url
    #             if url:
    #                 print(url.group(0))
    #                 yield scrapy.Request(url=url.group(0),callback=self.parse_sku)
    # def parse_list(self,response):

    #     urlLists = response.xpath(pageRule).extract()

    #     for url in urlLists:        # 遍历商品列表
    #         yield scrapy.Request(url=url,callback=self.parse_sku)

    #     nxtpgUrl = response.xpath("//body/div[3]/div[3]/div[@class='pages']/a[text()='下一页']/@href").extract_first() # 下一页
    #     if nxtpgUrl is not None:
    #         yield scrapy.Request(url=nxtpgUrl,callback=self.parse_list)

    def parse_sku(self,response):
        if re.compile(pageRule).match(response.url):
            item = {}
            item['url'] = response.url
            with open("D:/Product/Code/Python/pythonscraping/GLSpider/GLSpider/cfg.json",'r') as f:
                cfg_dict = json.load(f)[0]
       
            for k in cfg_dict.keys():
                try:
                    item[k] = response.xpath(cfg_dict[k]).extract_first().strip("\n").strip(" ")
                except:
                    pass
            yield item
        else:
            pass