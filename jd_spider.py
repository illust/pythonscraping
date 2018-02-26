#coding=utf-8
#import pandas as pd 
#import re
#import time
import urllib.request
from bs4 import BeautifulSoup
import socket


bookUrl = []
bookInfo = []

# 设置socket层的超时时间为20秒，在request.read()超时后能自动往下继续跑
socket.setdefaulttimeout(20) 

# 京东网页搜索python
InitUrl = "https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=2&s=1&click=0"

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
headers = {"user_agent":user_agent}

request = urllib.request.Request(url=InitUrl,headers=headers)

response = urllib.request.urlopen(request)
		
# 解析爬取内容
soup = BeautifulSoup(response,"html.parser")
books = soup.find_all("li",{"class":"gl-item"})

i=0
for item in books:
    i = i + 1
    print(i)
    print(item)
#    print(item.contents[1].get('href'))
#    print(item.contents[1].get('title'))
    print('\n')


