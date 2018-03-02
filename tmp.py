# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib.request
import socket

socket.setdefaulttimeout(20)

url = 'http://product.dangdang.com/1224472270.html'

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}

class skuInfo:

	soup = ""
	title = ""	# 单品名称
	price = ""  # 单品价格
	skuDtls = [] # 单品所有信息

	def __init__(self,url):
		self.url = url

	# 使用bs4解析html页面
	def parse(self):
		request = urllib.request.Request(self.url,headers=headers)
		response = urllib.request.urlopen(request)
		self.soup = BeautifulSoup(response,"html.parser")
		# self.soup = BeautifulSoup(open(self.url),"html.parser")

	def extractInfo(self):
		skuDetails = self.soup.find_all("div",class_="pro_content",id="detail_describe")[0].find("ul",class_="key clearfix")
		self.title = self.soup.find("h1").get("title") # 单品名称
		self.price = self.soup.find("div",class_="price_d").get_text()[4:].strip("\n") # 单品价格
		self.skuDtls.append(self.title)
		self.skuDtls.append(self.price)

		for item in skuDetails.find_all("li"): 	# 单品相关信息
			self.skuDtls.append(item.get_text())

	def infoShow(self):
		print("产品名称：%s"%self.skuDtls[0])
		print("产品价格：%s"%self.skuDtls[1])
		print("产品相关信息：%s"%self.skuDtls[2:])

si = skuInfo(url)
si.parse()
si.extractInfo()
si.infoShow()