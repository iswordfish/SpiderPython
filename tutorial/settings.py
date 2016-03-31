# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

ITEM_PIPELINES = {
    'tutorial.pipelines.JsonWithEncodingCnblogsPipeline': 300,
    'tutorial.pipelines.MySQLStoreCnblogsPipeline': 301,
    'tutorial.sgfpipelines.JsonWithEncodingSgfPipeline': 305,

}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 0.25
# start MySQL database configure setting
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'Blog'
MYSQL_USER = 'root'
MYSQL_PASSWD = '1234'
# end of MySQL database configure setting