# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import FormRequest, Request
from selenium import webdriver
import requests
#from WeiboCrawler.items import WeiboItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    loginUrl = 'http://www.weibo.com/login.php'
    
    # 构建浏览器
    chromePath = 'D:\Software\Continuum\Anaconda3\chromedriver.exe'
    wd = webdriver.Chrome(executable_path=chromePath)
    wd.get(loginUrl)
    wd.find_element_by_xpath('//*[@id="loginname"]').send_keys('illust0130@foxmail.com')
    wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('wwhh131134')
    wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').send_keys(input("输入验证码： "))
    wd.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    
    
    def start_requests(self):

        start_url = ["https://weibo.com/topgirls8?topnav=1&wvr=6&topsug=1",]
        yield scrapy.Request(url=start_url,cookies=wd.get_cookies(),callback=self.parse)
    
    def parse(self,response):
        item = {}
        item['url'] = response.url
        item['id'] = response.xpath('//*[@id="Pl_Official_Headerv6__1"]/div[1]/div/div[2]/div[2]/h1/text()').extract_first()
        item['introduce'] = response.xpath('//*[@id="Pl_Core_UserInfo__6"]/div/div/div[2]/div/div/ul/li[2]/span[2]/text()').extract_first()
        yield item
    
    
