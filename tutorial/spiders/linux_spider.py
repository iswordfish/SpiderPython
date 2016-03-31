#coding:utf-8

''''
linux中国内容爬去
'''
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle #用于定义需要提取的链接
from tutorial.items import *
from scrapy.selector import Selector


class LinuxSpider(CrawlSpider):
    name = "linux"
    allowed_domains = ["linux.cn"]
    start_urls = ['https://linux.cn/tech/index.php?page=2']
    rules = [ Rule(sle(allow=('/tech/index.php\?page=\d{1,3}'),), follow=True,callback='parse_item1') ]


    def parse_item1(self, response):
        print u'?????????????????????'
        sel = Selector(response)
        sites = response.xpath('//div[@class="block"]')
        items = []
        # postTitle = sel.css('div.day div.postTitle')
        for index in range(len(sites)):
            item = SgfPython()
            # item['title'] = sel.xpath('//span/text()').extract()[0]
            item['title'] = sites[index].css('p').xpath('text()').extract()[0]
            # item['title'] = sites[index].css("a").xpath('text()').extract()[0]
            items.append(item)
        return items
