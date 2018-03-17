# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib.request
import socket
import json
import requests



# 使用BeautifulSoup工具解析url
class bsParse:

	def __init__(self,url):
		self.url = url
		self.soup = ""

	def parse(self):

		socket.setdefaulttimeout(20)
		user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
		headers = {"user_agent":user_agent}

		response = requests.get(self.url,headers=headers)
		self.soup = BeautifulSoup(response.text,"html.parser")

		classify_left = self.soup.find_all("div",class_="classify_left")	# 当当网分类页左，右两部分
		classify_right = self.soup.find_all("div",class_="classify_right")

		cbooks = classify_left[0].find_all("div",class_="classify_books",recursive=False)

		return cbooks

# 利用解析得到的html构建当当网所有商品三级目录，以及第三级目录对应的url编号
class getCtg:

	cat_1 = {}

	def __init__(self,cbooks):
		self.classify_books = cbooks

	# 三层目录，使用三级嵌套结构
	def ctgParse(self):
		
		for i in range(len(self.classify_books)):
			ct1 = self.classify_books[i].find("a").get_text() # 第一层目录，比如 图书等等
			classify_kind = self.classify_books[i].find_all("div",class_="classify_kind",recursive=False)
			cat_2 = {}
			for j in range(len(classify_kind)):
				ct2 = classify_kind[j].find("a").get_text() # 第二层目录，比如 青春文学等等
				classify_kind_detail = classify_kind[j].find_all("ul",class_="classify_kind_detail")
				cat_3 = {}
				for item in classify_kind_detail[0]:
					cat_3[item.get_text()] = item.find('a').get('href')[29:-5] # 第三层目录，比如 校园等等，与对应url映射
				cat_2[ct2] = cat_3
			self.cat_1[ct1] = cat_2 

	# 保存到json中
	# def saveJson(self):
	# 	jsObj = json.dumps(self.cat_1,ensure_ascii=False)
	# 	fileObj = open('categories.json','w')
	# 	fileObj.write(jsObj)
	# 	fileObj.close()
	def showDict(self):
		print(self.cat_1)



