# -*- coding: utf-8 -*-

# eSpider项目scrapy配置文件


# 爬虫初始url，利用正则表达式对url形式进行匹配
# 匹配到www.epet.com，则进行整站爬取
# 匹配到list.epet.com，则对该分类目录下所有商品进行爬取
# 匹配到item.epet.com，则对该商品sku进行爬取
# 其他情况则引起异常，爬虫退出
START_URLS = ["epet.com"]

# 限制站点
ALLOWED_DOMAINS = 'epet.com'


# Scrapy项目实现的bot的名字。用来构造默认 User-Agent，同时也用来log。
# 当你使用 startproject 命令创建项目时其也被自动赋值。
BOT_NAME = 'eSpider'

SPIDER_MODULES = ['eSpider.spiders']
NEWSPIDER_MODULE = 'eSpider.spiders'

# 默认: False
# 是否遵循robots协议
ROBOTSTXT_OBEY = False

# 输出文件编码格式
FEED_EXPORT_ENCODING = 'utf-8'


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
# 默认: "Scrapy/VERSION (+http://scrapy.org)"
# 爬取的默认User-Agent，除非被覆盖。


# Scrapy downloader并发请求(concurrent requests)的最大值，默认为16
CONCURRENT_REQUESTS = 32 

# Item Pipeline同时处理item的最大值，默认为100
# CONCURRENT_ITEMS = 1


# 对单个网站进行并发请求的最大值，默认为8
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 对单个IP进行并发请求的最大值。默认为0，如果非0，则忽略CONCURRENT_REQUESTS_PER_DOMAIN 设定， 
# 使用该设定。 也就是说，并发限制将针对IP，而不是网站。
# 该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0，下载延迟应用在IP而不是网站上。 
# CONCURRENT_REQUESTS_PER_IP = 16

# 关闭cookies，默认是打开状态
# COOKIES_ENABLED = False

# 关闭telnet console，默认是打开状态
# TELNETCONSOLE_ENABLED = False

# Scrapy HTTP Request使用的默认header。由 DefaultHeadersMiddleware 产生。
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# DEFAULT_ITEM_CLASS
# 默认: 'scrapy.item.Item'
# the Scrapy shell 中实例化item使用的默认类。

# DOWNLOADER
# 默认: 'scrapy.core.downloader.Downloader'
# 用于crawl的downloader.

# DOWNLOADER_MIDDLEWARES
# 默认:: {}
# 保存项目中启用的下载中间件及其顺序的字典。

# DOWNLOAD_DELAY
# 默认: 0
# 下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数

# DOWNLOAD_HANDLERS
# 默认: {}
# 保存项目中启用的下载处理器(request downloader handler)的字典。

# DOWNLOAD_TIMEOUT
# 默认: 180
# 下载器超时时间(单位: 秒)。

# EXTENSIONS
# 默认:{}
# 保存项目中启用的插件及其顺序的字典。


# ITEM_PIPELINES
# 默认: {}
# 保存项目中启用的pipeline及其顺序的字典。该字典默认为空，值(value)任意。 
# 不过值(value)习惯设定在0-1000范围内。值越小优先级越高。
# 下面设定启用去重功能
ITEM_PIPELINES = {
   'eSpider.pipelines.DuplicatesPipeline': 300,
}

# ITEM_PIPELINES_BASE
# 默认: {}
# 保存项目中默认启用的pipeline的字典。永远不要在项目中修改该设定，而是修改 ITEM_PIPELINES。

# LOG_ENABLED
# 默认: True
# 是否启用logging。

# LOG_ENCODING
# 默认: 'utf-8'
# logging使用的编码。

# LOG_FILE
# 默认: None
# logging输出的文件名。如果为None，则使用标准错误输出(standard error)。

# LOG_FORMAT
# 默认: '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# 日志的数据格式

# LOG_DATEFORMAT
# 默认: '%Y-%m-%d %H:%M:%S'
# 日志的日期格式

# LOG_LEVEL
# 默认: 'DEBUG'
# log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG。

# LOG_STDOUT
# 默认: False
# 如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中。

# RANDOMIZE_DOWNLOAD_DELAY
# 默认: True
# 如果启用，当从相同的网站获取数据时，Scrapy将会等待一个随机的值 (0.5到1.5之间的一个随机值 * DOWNLOAD_DELAY)。
# 该随机值降低了crawler被检测到(接着被block)的机会。某些网站会分析请求， 查找请求之间时间的相似性。

# REDIRECT_MAX_TIMES
# 默认: 20
# 定义request允许重定向的最大次数。超过该限制后该request直接返回获取到的结果。对某些任务我们使用Firefox默认值。



# SCHEDULER
# 默认: 'scrapy.core.scheduler.Scheduler'
# 用于爬取的调度器。

# SPIDER_MIDDLEWARES
# 默认: {}
# 保存项目中启用的下载中间件及其顺序的字典。


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'eSpider.middlewares.EspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'eSpider.middlewares.EspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html

# issue1 code
# EXTENSIONS = {
#    'eSpider.extensions.closespider.CloseSpider': 500,
# }
# ITEM_COUNT = 10

# issue1相关代码
# EXTENSIONS = {
#    'eSpider.droppeditem.DroppedItemCloseSpider':500,
# }
# CLOSESPIDER_DROPPEDITEMCOUNT = 200



# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'eSpider.pipelines.EspiderPipeline': 300,
#}


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
