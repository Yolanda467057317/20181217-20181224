# -*- coding: utf-8 -*-

# Scrapy settings for CQJob project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'CQJob'

SPIDER_MODULES = ['CQJob.spiders']
NEWSPIDER_MODULE = 'CQJob.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
REFERER = 'https://www.lagou.com/jobs/list_?px=default&city=%E6%9D%AD%E5%B7%9E'
COOKIE = 'user_trace_token=20190716135550-4cc42e65-1e72-430c-9564-5bffc97683ad; _ga=GA1.2.1539741695.1563256553; LGUID=20190716135552-5e43c1fb-a78e-11e9-a4e5-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216bf95d8db33d0-0a84e479f08c2f-e343166-1049088-16bf95d8db41f0%22%2C%22%24device_id%22%3A%2216bf95d8db33d0-0a84e479f08c2f-e343166-1049088-16bf95d8db41f0%22%7D; LG_LOGIN_USER_ID=13d6db3616d8da36c5a4a0e104fbaaa7f6eca5d58e2d6f9e041b170394a1016f; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=cc5f8635533e16300353fb95de0cca686e89d328c733d42546371d67e0cad82b; privacyPolicyPopup=false; index_location_city=%E6%9D%AD%E5%B7%9E; JSESSIONID=ABAAABAAADEAAFI246B1F4B345BDA725331AF270F7B0CBF; _putrc=9CFD5970A9C1BA77123F89F2B170EADC; login=true; unick=%E8%8B%9F%E9%91%AB; _gid=GA1.2.1929946501.1563593731; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563256781,1563259567,1563263933,1563593731; TG-TRACK-CODE=search_code; LGSID=20190720192140-8bfcf5ac-aae0-11e9-812b-525400f775ce; X_HTTP_TOKEN=1485d46e6157d9b88973263651c241eb6c52e98ff0; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563623818; _gat=1; LGRID=20190720195656-792bf850-aae5-11e9-a4eb-5254005c3644; SEARCH_ID=d45fdc7f4bd24bdf888af9bc49207f85'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
   'CQJob.pipelines.CqjobPipeline': 300,
}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

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
#    'CQJob.middlewares.CqjobSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'CQJob.middlewares.CqjobDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'CQJob.pipelines.CqjobPipeline': 300,
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
