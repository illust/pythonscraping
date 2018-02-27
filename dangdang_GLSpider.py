# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import urllib.request
import socket

# socket.setdefaulttimeout(20)

# url = 'http://category.dangdang.com/'

# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
# headers = {"user_agent":user_agent}

# request = urllib.request.Request(url,headers=headers)
# reponse = urllib.request.urlopen(request)
# soup = BeautifulSoup(reponse,"html.parser")


reponse = "D:\categories.html"
soup = BeautifulSoup(open(reponse),"html.parser")


leftCtgs = soup.find_all("div",class_="classify_left")	# 当当网分类页左，右两部分
rightCtgs = soup.find_all("div",class_="classify_right")

# i = 0
# for item in leftCtgs[0].div.children:
# 	i = i + 1
# 	print(i)
# 	ims = item.find_all("a",href=re.compile("^http://category.*?html$"))
# 	for im in ims:
# 		print(im.get_text())
# 		#print("\n")
# 	print('\n')
bigCtgs = []
lgoodsCtgs = leftCtgs[0].find_all("div",{"class":"classify_books_detail"})
rgoodsCtgs = rightCtgs[0].find_all("div",{"class":"classify_books_detail"})

for item in lgoodsCtgs:
	bigCtgs.append(item.get_text())
	print(item.get_text())
	print('\n')

for item in rgoodsCtgs:
	bigCtgs.append(item.get_text())
	print(item.get_text())
	print('\n')

print(bigCtgs)
