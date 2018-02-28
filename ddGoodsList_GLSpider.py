# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib.request

response = "D:\goodslist.html"
soup = BeautifulSoup(open(response),"html.parser")

# 获得商品单品信息与对应的网页地址
books = soup.find_all('a',href=re.compile("^http://product.*?html$"),dd_name="单品图片")		
booksDict = {}
i = 0
for item in books:
	i = i + 1
	bookUrl=item.get('href')
	bookInfo=item.get('title')
	booksDict[bookInfo] = bookUrl

# 获得该目录所有商品总页数
buttomPage = soup.find_all("ul",dd_name="底部翻页")[0] #
pageNum = buttomPage.find_all("a")
li = []
for item in pageNum:
	li.append(item.get_text())
pageNum = int(li[-2])