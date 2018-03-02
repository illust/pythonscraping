# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib.request
import socket
import json
import requests


socket.setdefaulttimeout(20)
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}

url = 'http://category.dangdang.com/cp01.54.06.00.00.00.html'
#url = "D:\goodslist.html"


class getSku:

	soup = ""
	pageNum = 0
	pgUrl = {}
	booksDict = {}

	def __init__(self,url):
		self.url = url

	def getPgUrl(self):
		return self.pgUrl

	def getPageNum(self):
		return self.pageNum

	def getSoup(self):
		return self.soup

	# 使用bs4解析html页面
	def parse(self):
		#request = urllib.request.Request(self.url,headers=headers)
		#response = urllib.request.urlopen(request)
		response = requests.get(self.url,headers=headers)
		self.soup = BeautifulSoup(response.text,"html.parser")
		#self.soup = BeautifulSoup(open(self.url),"html.parser")

	# 获得该目录所有商品总页数
	def PageNum(self):
		bp = self.soup.find_all("a",{"name":"bottom-page-turn"})
		li = []
		for item in bp:
			li.append(item.get_text())
		self.pageNum = int(li[-1])

	# 遍历某分类目录下多页商品
	# 有些目录页数过多，暂取前一部分网页商品信息
	# def lookAllPage(self):
		
	# 	if self.pageNum <= 20:	# 页数大于等于2且小于等于20页时
	# 		if self.pageNum >= 2:
	# 			pageList = []
	# 			for p in range(2,self.pageNum+1):
	# 				pageList.append("pg"+str(p)+"-"+self.url[29:-5])
	# 			self.pgUrl[self.url[29:-5]] = pageList
	# 		elif self.pageNum == 1:
	# 			self.pgUrl[self.url[29:-5]] = self.url[29:-5] 
	# 	elif self.pageNum > 20:	# 页数大于20时，只取前20页
	# 		pageList = []
	# 		for p in range(2,21):
	# 			pageList.append("pg"+str(p)+"-"+self.url[29:-5])
	# 		self.pgUrl[self.url[29:-5]] = pageList

	# 获得商品单品信息与对应的网页地址映射，存储在bookDict字典中
	# 传入的参数为商品目录页url
	def getSkuUrl(self):

		books = self.soup.find_all('a',href=re.compile("^http://product.*?html$"),dd_name=u"单品图片")		
		i = 0
		for item in books:
			i = i + 1
			bookUrl=item.get('href')[28:-5]
			bookInfo=item.get('title')
			self.booksDict[bookInfo] = bookUrl
		return self.booksDict

	# 保存三级分类下某一页所有商品及其链接到json中
	def saveBooksDictJson(self):
		jsObj = json.dumps(self.booksDict,ensure_ascii=False)
		fileObj = open('booksDict.json','w')
		fileObj.write(jsObj)
		fileObj.close()

	# 保存三级分类所有网页链接
	def savePageUrl(self):
		jObj = json.dumps(self.pgUrl,ensure_ascii=False)
		fObj = open('pageUrl.json','w')
		fObj.write(jObj)
		fObj.close()

# p = getSku(url)
# p.parse()
# print(p.getSoup())
# p.PageNum()
# print(p.getPageNum())
# p.lookAllPage()
# print(p.getPgUrl())
# p.getSkuUrl()
# print(p.getSkuUrl())
# p.saveBooksDictJson()
