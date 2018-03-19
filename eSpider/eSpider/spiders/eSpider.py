# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.exceptions import CloseSpider  # 爬虫定量停止功能未完成 issue1
import requests
from scrapy import Selector


class epetWholeSpider(scrapy.Spider):

    name = 'epet'
    allowed_domains = ['epet.com']
    
    # 针对eSpider的pipeline
    custom_settings = {
        'ITEM_PIPELINES':{
            'eSpider.pipelines.DuplicatesPipeline':400
        }
    }
    # 从命令行输入url
    def __init__(self,*args,**kwargs):
        super(epetWholeSpider,self).__init__(*args,**kwargs)
        self.start_urls = [kwargs.get('start_urls')]

        # 输入url检错功能未完成 issue2
        # lnk = kwargs.get('start_urls')
        # if re.compile(r'http://www.epet.com').match(lnk) == None:
        #     raise CloseSpider()
        # else:
        #     self.start_urls = [kwargs.get('start_urls')]
        
    # issue1
    # def __init__(self):
    #   self.count = 0 # 设置item初始个数
    #   self.max_count = 20 # 设置最大个数
    

    def parse(self,response):

        links = response.xpath("//a")
        for link in links:

            # 提取url
            url = link.xpath("./@href").extract_first()
            if url == None:
                pass  
            else:
                _link = re.compile(r'http://list.epet.com/[^(search)][^\s]+').match(url) # 利用正则表达式匹配 list.epet.com
                # 如果url匹配到，则进行相应操作
                if _link:
                    item = {}
                    # 获得链接内部文本
                    text = link.xpath(".//text()").extract_first()
                    # 重新发起一个请求，查看该list页面是否为空（不含任何商品）
                    res = requests.get(_link.group(0))
                    flg = Selector(res).xpath("//body/div[3]/div[3]/div[@class='bgwhite']/@class").extract_first()
                    # 如果为空，则该分类目录下无商品，视为无效，否则保存链接，继续其他操作
                    if flg == 'bgwhite':
                        pass
                    else:
                        # if text == None:
                        #     item["link_text"] = None
                        # else:
                        #     item["link_text"] = text.strip(" ").strip("\n")
                        # item["link"] = _link.group(0)
                        yield scrapy.Request(url=_link.group(0),callback=self.parse_list)
                        yield scrapy.Request(url=_link.group(0),callback=self.parse)
    
                        # yield item

                        # issue1
                        # self.count = self.count + 1
                        # if self.count == self.max_count:
                        #   raise CloseSpider('The number of extracted data is enough!')

    def parse_list(self,response):

        urlLists = response.xpath("//a[@class='gtitle']//@href").extract()

        for url in urlLists:        # 遍历商品列表
            yield scrapy.Request(url=url,callback=self.parse_sku)

        nxtpgUrl = response.xpath("//body/div[3]/div[3]/div[@class='pages']/a[text()='下一页']/@href").extract_first() # 下一页
        if nxtpgUrl is not None:
            yield scrapy.Request(url=nxtpgUrl,callback=self.parse_list)

    def parse_sku(self,response):
        item = {}

        title = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/h1[@id='abcde']/text()").extract_first().strip("\n").strip(" ")
        subtitle = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/div[@class='ft14 mt c93c']/text()").extract_first()
        
        categories = []
        ctg1 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[1]/span/text()").extract()
        ctg2 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[2]/span/text()").extract()
        ctg3 = response.xpath("//body/div[@class='w-max ct mb20']/div[1]/div[1]/div[3]/span/text()").extract()
        categories.append(ctg1[0]+"->"+ctg2[0]+"->"+ctg3[0].strip("\r").strip("\n").strip(" "))
        
        price = response.xpath("//body/div[@class='w-max ct mb20']/div[2]/div[2]/div[2]/div[2]/span[@id='goods-sale-price']/text()").extract_first()
        
        taglist = response.xpath("//div[@class='gdicos mt pb10 pointer']//text()").extract()
        tag = [i.strip('\n').strip() for i in taglist]
        tag = [i for i in tag if i !='']    # 去空格回车
        
        if title == None:
            item['title'] = None
        else:
            item['title'] = title
        item['subtitle'] = subtitle
        item['url'] = response.url
        item['categories'] = categories
        item['price'] = price
        item['tag'] = tag 

        yield item




