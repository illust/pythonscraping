# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib.request
import socket
import sys 

socket.setdefaulttimeout(20)


url = 'http://category.dangdang.com/cp01.54.06.00.00.00.html'

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}

encoding = "gb18030"

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8',errors='replace')
soup = BeautifulSoup(html,"html.parser")

# bp = soup.find_all("a",{"name":"bottom-page-turn"})
# print(bp)
# li = []
# for item in bp:
# 	li.append(item.get_text())
# 	print('\n')

# print(int(li[-1]))

url = soup.find_all('a',href=re.compile("^http://product.*?html$"))
for i in url:
	print(i.get_text())
	print('\n')


