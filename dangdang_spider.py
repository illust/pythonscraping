#coding=utf-8
import pandas as pd 
import re
import time
import urllib.request
from bs4 import BeautifulSoup

url = "http://search.dangdang.com/?key=java&act=input&page_index="
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}
index = 2
booksDict = {}
booksDf = pd.DataFrame(columns=["url","bookInfo"])
while index <= 10:
	# 发起请求
	request = urllib.request.Request(url=url+str(index),headers=headers)
	response = urllib.request.urlopen(request)
	index = index + 1

	# 解析爬取内容
	soup = BeautifulSoup(response,"html.parser")
	books = soup.find_all('a',href=re.compile("^http://product.*?html$"),dd_name="单品标题")
	for item in books:
		url = item.get('href')
		bookInfo = item.get('title')
		booksDict.update(url=bookInfo)

		# print(item.get('href'))
		# print(item.get('title'))

		#print("##############################################################################################################")
		#all_books.append(item.get('href'))
	time.sleep(1) # 休眠1秒

#booksDf.to_csv("dangdangBook.csv")
for item in booksDict:
	print(item,'\n')
	print(booksDict[item])
	print('********************************************************************************************')