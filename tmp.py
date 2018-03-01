# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
import urllib.request
import socket

socket.setdefaulttimeout(20)

url = 'http://product.dangdang.com/24003310.html'

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
soup = BeautifulSoup(response,"html.parser")

skuDetails = soup.find_all("div",class_="pro_content",id="detail_describe")[0].find("ul",class_="key clearfix")

sd = []

for item in skuDetails.find_all("li"):
	sd.append(item.get_text())

print(sd)

price = soup.find()