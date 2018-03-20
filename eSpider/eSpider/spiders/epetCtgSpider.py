# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Selector
import requests

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

        # js异步加载获取参数表格数据, some tricks
        lnk = "http://item.epet.com/goods.html?do=GetParamsAndAnnounce&gid=" + str(re.compile('[0-9]+').findall(response.url)[0])
        res = requests.get(lnk)
        cnt = Selector(res).xpath("//body/div[1]/div[@id='goods_params']/table/tr/td")
        plist = []
        j=0
        for i in cnt:
            txt = i.xpath("text()").extract_first().strip("\n").strip()
            if len(txt) == 0:
                txt = i.xpath("//div[@class]/span/text()").extract()[j]
                j = j + 1
            plist.append(txt)
        pnames = []
        params = []
        for i in range(len(plist)):
            if i%2 == 0:
                pnames.append(plist[i])
            else:
                params.append(plist[i])
        paramsDict = dict(zip(pnames, params))

        if title == None:
            item['title'] = None
        else:
            item['title'] = title
        item['subtitle'] = subtitle
        item['url'] = response.url
        item['categories'] = categories
        item['price'] = price
        item['tag'] = tag
        item['otherParams'] = paramsDict

        yield item

            
            