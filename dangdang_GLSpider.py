# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import urllib.request
import socket

socket.setdefaulttimeout(20)

url = 'http://category.dangdang.com/'

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response,"html.parser")


# response = "D:\categories.html"
# soup = BeautifulSoup(open(response),"html.parser")


classify_left = soup.find_all("div",class_="classify_left")	# 当当网分类页左，右两部分
classify_right = soup.find_all("div",class_="classify_right")


cbooks = classify_left[0].find_all("div",class_="classify_books",recursive=False)

class GetCtg:
	def __init__(self,cbooks):
		self.classify_books = cbooks

	def CtgShow(self):
		cat_1 = {}
		for i in range(len(self.classify_books)):
			ct1 = self.classify_books[i].find("a").get_text() # 第一层目录，比如 图书等等
			classify_kind = self.classify_books[i].find_all("div",class_="classify_kind",recursive=False)
			cat_2 = {}
			for j in range(len(classify_kind)):
				ct2 = classify_kind[j].find("a").get_text() # 第二层目录，比如 青春文学等等
				classify_kind_detail = classify_kind[j].find_all("ul",class_="classify_kind_detail")
				cat_3 = []
				for item in classify_kind_detail[0]:
					cat_3.append(item.get_text()) # 第三层目录，比如 校园等等
				cat_2[ct2] = cat_3
			cat_1[ct1] = cat_2 
		print(cat_1)

Instance = GetCtg(cbooks)
Instance.CtgShow()

