#coding:utf-8
'''
豆瓣电影爬去
'''
import scrapy
from scrapy.utils.response import get_base_url
from tutorial.items import *

from scrapy.contrib.spiders import CrawlSpider, Rule

from scrapy.selector import Selector

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from tutorial.items import ZhihuItem
from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.spiders import Spider

class DmozSpider(Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://www.douban.com/people/141360318/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        print  'okkkkk**************************'
        sel = Selector(response)
        sites = sel
        items = []

        # for site in sites:
        item = Website()
        item['name'] =sel.css("a").xpath('text()').extract()[0]
        item['url'] = sel.xpath('a/@href').extract()
        item['description'] = sel.xpath('text()').re('-\s[^\n]*\\r')
        items.append(item)

        return items