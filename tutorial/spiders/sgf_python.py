#coding:utf-8
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle #用于定义需要提取的链接
from tutorial.items import *
from scrapy.selector import Selector


class DmozSpider(CrawlSpider):
    name = "demo"
    allowed_domains = ["360.cn"]
    # start_urls=["http://bobao.360.cn/learning/index&page=1"]
    start_urls = ['http://bobao.360.cn/news/&page=2']
    rules = [ Rule(sle(allow=('&page=\d{1,3}'),), follow=True,callback='parse_item1') ]
    # rules=[	Rule(sle(allow=("/learning/index&page=\d{1,3}")),follow=True,callback='parse_item')]

#<a href="&page=3">3</a>

    def parse_item1(self, response):
        print u'?????????????????????'
        sel = Selector(response)
        sites = sel.xpath('//*')
        items = []
        #下一页
        for site in sites:
            item = SgfPython()
            item['title'] = site.xpath('//*[@id="all-news-list"]/li[2]/div/a/text()').extract()
            # item['link'] =site.xpath('section/div/h2/a/@href').extract()
            items.append(item)
        return items



class bobao_spider(CrawlSpider):
    name="bobao"
    allowed_domains=["360.cn"]
    start_urls=["http://bobao.360.cn/learning/index&page=1"]
    rules=[	Rule(sle(allow=("/learning/index&page=\d{1,3}")),follow=True,callback='parse_item')
     ]#定义提取链接的规则，继续跟进，提取到的链接回调给parse_item函数作为参数

    def parse_item(self,response):
       print u'这是谁?????????????????????'

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle #用于定义需要提取的链接


class NewsSpider(CrawlSpider):
    name = "demo2"
    allowed_domains = ["360.cn"]
    # start_urls=["http://bobao.360.cn/activity/index&page=2"]#这个连接测试成功
    start_urls=["http://bobao.360.cn/vul/index?type=all&page=1"]#
    rules = [ Rule(sle(allow=(r'/vul/index\?type=all&page=\d{1,3}')), follow=True,callback='parse_item1') ]#这个测试不成功原因好像
    #allow=r'/vul/index?type=all&page=\d{1,3} 这个里面/vul/index?这个?有影响,请教如何修改
    # rules = [ Rule(sle(allow=r'/activity/index&page=\d{1,3}'), follow=True,callback='parse_item1') ]#这个连接测试成功

#/activity/index&page=

    def parse_item1(self, response):
        print u'这是谁?????????????????????'
        sel = Selector(response)
        sites = sel.xpath('//*[@id="qa"]')
        items = []
        #下一页
        for site in sites:
            item = SgfPython()
            item['title'] = site.xpath('//title/text()').extract()
            # item['link'] =site.xpath('section/div/h2/a/@href').extract()
            items.append(item)
        return items

class MySpider1(CrawlSpider):

    name = "huhu"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/huhuuu",
    ]


    rules = (
        # 提取匹配 huhuuu/default.html\?page\=([\w]+) 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(sle(allow=(r'huhuuu/default.html\?page\=([\w]+)', ),),callback='parse_item'),

        # 提取匹配 'huhuuu/p/' 的链接并使用spider的parse_item方法进行分析
        # Rule(sle(allow=('huhuuu/p/', )), callback='parse_item'),
    )

    def parse_item(self, response):
        print u'这是谁?????????????????????'







