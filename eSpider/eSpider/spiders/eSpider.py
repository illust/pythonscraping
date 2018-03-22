# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.exceptions import CloseSpider  # 爬虫定量停止功能未完成 issue1
import requests
from scrapy import Selector


class epetWholeSpider(scrapy.Spider):

    name = 'epet'
    # 针对eSpider的pipeline
    custom_settings = {
        'ITEM_PIPELINES':{
            'eSpider.pipelines.DuplicatesPipeline':400
        }
    }

    # 解析初始url格式
    def start_requests(self):

        self.count = 0 # 设置item初始个数
        self.max_count = 500 # 设置最大个数

        allowed_domains = self.settings.get('ALLOWED_DOMAINS')[0]

        start_urls = self.settings.get('START_URLS')
        if re.compile(r'http://www.epet.com').match(start_urls[0]):
            return [scrapy.Request(start_urls[0],callback=self.parse)]
        elif re.compile(r'http://list.epet.com').match(start_urls[0]):
            return [scrapy.Request(start_urls[0],callback=self.parse_list)]
        elif re.compile(r'http://item.epet.com').match(start_urls[0]):
            return [scrapy.Request(start_urls[0],callback=self.parse_sku)]
        else:
            raise CloseSpider("start url is wrong!")

        

    
    # 从命令行输入url功能
    # def __init__(self,*args,**kwargs):
    #     super(epetWholeSpider,self).__init__(*args,**kwargs)
    #     self.start_urls = [kwargs.get('start_urls')]
    

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
                        yield scrapy.Request(url=_link.group(0),callback=self.parse_list)
                        yield scrapy.Request(url=_link.group(0),callback=self.parse)

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

        self.count = self.count + 1
        if self.count <= self.max_count:
            yield item
        else:
            raise CloseSpider("Item is enough!")




