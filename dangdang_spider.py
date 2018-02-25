#coding=utf-8
import pandas as pd 
import re
import time
import urllib.request
from bs4 import BeautifulSoup
import socket  


socket.setdefaulttimeout(20) # 设置socket层的超时时间为20秒，在request.read()超时后能自动往下继续跑
url = "http://search.dangdang.com/?key=python&act=input&page_index="
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}
index = 2
booksDict = {}

bookUrl = []
bookInfo = []
i = 0
while index <= 10:
	# 发起请求
	request = urllib.request.Request(url=url+str(index),headers=headers)
	
	try:
		response = urllib.request.urlopen(request)
		
		# 解析爬取内容
		soup = BeautifulSoup(response,"html.parser")
		books = soup.find_all('a',href=re.compile("^http://product.*?html$"),dd_name="单品标题")
		
		for item in books:
			i = i + 1
			bookUrl.append(item.get('href'))
			bookInfo.append(item.get('title'))
			
			
			# print(i)
			# print(bookUrl)
			# print(bookInfo)
		response.close()    # 注意关闭response
	except urllib.error.URLError as e:
		print(e.reason) 

	index = index + 1
	time.sleep(1) # 休眠1秒

booksDict = {"bookUrl":bookUrl,"bookInfo":bookInfo}
booksDf = pd.DataFrame(booksDict,columns=["bookUrl","bookInfo"],index=range(1,i+1))
booksDf.to_csv("dangdangBook.csv")
# for item in booksDict:
# 	print(item,'\n')
# 	print(booksDict[item])
# 	print('********************************************************************************************')