# -*- coding: utf-8 -*-

# Scrapy settings for week02_01 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'week02_01'

SPIDER_MODULES = ['week02_01.spiders']
NEWSPIDER_MODULE = 'week02_01.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'week02_01 (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3

DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'cookie': 'lxsdk_cuid=172f8655508c8-0b7c2e34487bb5-31617402-1aeaa0-172f8655509c8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593305290,1593306295; __mta=209484077.1593305290267.1593306456952.1593306708379.10; uuid_n_v=v1; iuuid=6A770690B8DD11EA9BBABBBB31B3B9ACB0CD4F6FB91249B48EB407DD5F7AB956; webp=true; ci=30%2C%E6%B7%B1%E5%9C%B3; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172f88207ab75b-03b63323e0c112-73236134-349920-172f88207ac7a9%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22172f88207ab75b-03b63323e0c112-73236134-349920-172f88207ac7a9%22%7D; _last_page=c_dmLad; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593307171; _lxsdk=6A770690B8DD11EA9BBABBBB31B3B9ACB0CD4F6FB91249B48EB407DD5F7AB956; __mta=209484077.1593305290267.1593306708379.1593307172384.11; _lxsdk_s=172f8655509-342-4cc-3f5%7C%7C31',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'week02_01.middlewares.Week0201SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'week02_01.middlewares.Week0201DownloaderMiddleware': 543,
# }
DOWNLOADER_MIDDLEWARES = {
    'week02_01.middlewares.Week0201DownloaderMiddleware': None,
    'week02_01.middlewares.RandomHttpProxyMiddleware': 750,

}
HTTP_PROXY_LIST = [
    'http://52.179.231.206:80',
    'http://95.0.194.241:9090',
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'week02_01.pipelines.Week0201Pipeline': 300,
# }
ITEM_PIPELINES = {
    'week02_01.pipelines.Week0201Pipeline': 300,
    'week02_01.pipelines.MySQLPipeline': 400,
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 自已定pipeline MySQL配置项
MYSQL_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'test',
    'charset': 'utf8mb4'
}
