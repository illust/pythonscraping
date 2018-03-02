# -*- coding: utf-8 -*-

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

bkDict = {}

for i in range(2,21):
	print(i)
	pageUrl = url[:29]+'pg'+str(i)+'-'+url[29:]
	p = getSku(pageUrl)
	p.parse()
	gs = p.getSkuUrl()
	bkDict['page'+str(i)] = gs
	print(gs)
	print('\n')
	# p.savePageUrl()

jsObj = json.dumps(bkDict,ensure_ascii=False)
fileObj = open('bkDict.json','w')
fileObj.write(jsObj)
fileObj.close()