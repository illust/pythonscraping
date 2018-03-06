# -*- coding: utf-8 -*-
"""Sven.
Usage:
  conSpider.py url <url> allCtg 
  conSpider.py url <url> allPage [--pageNum=N]
  conSpider.py url <url> skuInfo 
  conSpider.py (-h | --help)

Options:
  -h --help      show this screen.
  --pageNum=N    number of pages you want to extract.

"""

import re
from bs4 import BeautifulSoup
import urllib.request
import socket
import json
import requests
from docopt import docopt

# 非官方库
from getAllCtg import bsParse,getCtg
from getAllPages import getSku
from getSkuInfo import skuInfo



if __name__ == '__main__':

	args = docopt(__doc__)
	if args['url']:
		if args['allCtg']:	# e.g url = 'http://category.dangdang.com/'
			Instance = bsParse(args['<url>'])
			Instance = getCtg(Instance.parse())
			Instance.ctgParse()
			Instance.showDict()

		elif args['allPage']:	# e.g url = 'http://category.dangdang.com/cp01.54.06.00.00.00.html'
			inst = getSku(args['<url>'])
			inst.parse()
			inst.getSkuUrl()
			inst.showBooksDict()

		elif args['skuInfo']:   # e.g url = 'http://product.dangdang.com/1224472270.html'
			si = skuInfo(args['<url>'])
			si.parse()
			si.extractInfo()
			si.infoShow()






