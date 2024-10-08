# Scrapy settings for myproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import datetime
from re import S
BOT_NAME = "myproject"

SPIDER_MODULES = ["myproject.spiders"]
NEWSPIDER_MODULE = "myproject.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "myproject (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "myproject.middlewares.MyprojectSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "myproject.middlewares.MyprojectDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "myproject.pipelines.MyprojectPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# DOWNLOADER_MIDDLEWARES = {
#     # ... Other middlewares
#     # 'scratest.middlewares.UARotatorMiddleware': 400,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
# }

# # Desired file format
# FEED_FORMAT = "csv"
 
# # Name of the file where data extracted is stored, time is appended to avoid overwriting
# FEED_URI = "business_%(time)s.csv" % {'time': datetime.datetime.now().strftime('%Y%m%d%H%M%S')}


# SCRAPEOPS_API_KEY = 'd74c7df8-a747-468b-b6bc-594fd691e6eb'
# SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
# SCRAPEOPS_NUM_RESULTS= 100

# DOWNLOADER_MIDDLEWARES = {
#     'myproject.middlewares.MyprojectSpiderMiddleware': 400,
#     'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
# }
# EXTENSIONS = {
#     'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
# }
# Desired file format
# FEED_FORMAT = "csv"
 
# # Name of the file where data extracted is stored, time is appended to avoid overwriting
# FEED_URI = "infodoanhnghiep_%(time)s.csv" % {'time': datetime.datetime.now().strftime('%Y%m%d%H%M%S')}

RETRY_ENABLED = True
RETRY_HTTP_CODES = [429]  # Thử lại khi gặp lỗi 429
RETRY_TIMES = 5  # Số lần thử lại


FEEDS = {
    "s3://businessbucketscrapy/%(name)s/%(name)s_%(time)s.csv": {
    "format": "csv",
    }
}

AWS_ACCESS_KEY_ID = 'AKIA6DZW3JDPIZU4PYFX'
AWS_SECRET_ACCESS_KEY = '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'

# # start url
# START_URLS = [
#     "https://infodoanhnghiep.com/Da-Nang/",
# ]

# PAGE_START = 1
# PAGE_END = 500  # Ví dụ: Số trang kết thúc