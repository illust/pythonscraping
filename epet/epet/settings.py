# -*- coding: utf-8 -*-

# Scrapy settings for epet project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'epet'

SPIDER_MODULES = ['epet.spiders']
NEWSPIDER_MODULE = 'epet.spiders'

ALLOWED_DOMAINS = ['jd.com',]
START_URLS = ['https://www.jd.com']

# 爬取链接domain字段
RERULE = r'' #r'gallery-store-ALL.*?'
#RERULE = r'list.*?' 

# html文件存储文件夹
FOLDER = "jd"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'epet (+http://www.yourdomain.com)'


# 是否遵循robots.txt，通常设为False，不遵守
ROBOTSTXT_OBEY = False


# 输出文件编码格式
FEED_EXPORT_ENCODING = 'utf-8'


# Scrapy提前终止四个可选条件：

# 1)收到指定数目的响应之后终止爬虫
# CLOSESPIDER_PAGECOUNT = 50

# 2)抓取指定数码的Item之后终止爬虫
# CLOSESPIDER_ITEMCOUNT = 200

# 3)指定时间之后终止爬虫
# CLOSESPIDER_TIMEOUT=100

# 4)发生指定数目错误之后终止爬虫
# CLOSESPIDER_ERROR=10



# 向下载器并发发出的请求数目，默认为16
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'epet.middlewares.EpetSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'epet.middlewares.EpetDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'epet.pipelines.EpetPipeline': 300,
#}
ITEM_PIPELINES = {
	'epet.pipelines.html2FilePipeline': 100,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
