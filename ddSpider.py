import re
from bs4 import BeautifulSoup
import urllib.request
import socket
import json
from ddGoodsList_GLSpider import getSku

socket.setdefaulttimeout(20)

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}

url = 'http://category.dangdang.com/cp01.54.06.00.00.00.html'

for i in range(2,21):
	pageUrl = url[:29]+'pg'+str(i)+'-'+url[29:]
	p = getSku(pageUrl)
	p.parse()
	print("test...")
	print(p.getSoup().title)
	# p.PageNum()
	# #print(p.getPageNum())
	# p.lookAllPage()
	# #print(p.getPgUrl())
	# p.getSkuUrl()
	# #print(p.getSkuUrl())
	# p.savePageUrl()