#coding=utf-8
import re
import json
from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import *



class AdamSpider(CrawlSpider):

    name = "adam"
    allowed_domains = ["cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/linbinqiang/",
    ]


    rules = (
        # 提取匹配 huhuuu/default.html\?page\=([\w]+) 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(SgmlLinkExtractor(allow=('linbinqiang/default.html\?page\=([\w]+)', ),)),

        # 提取匹配 'huhuuu/p/' 的链接并使用spider的parse_item方法进行分析
        Rule(SgmlLinkExtractor(allow=('linbinqiang/p/', )), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=('linbinqiang/archive/', )), callback='parse_item'), #以前的一些博客是archive形式的所以
    )
    def parse_item(self, response):

        #print "-----------------"
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
        postTitle = sel.css('div.day div.postTitle')
        #print "=============length======="
        postCon = sel.css('div.postCon div.c_b_p_desc')
        #标题、url和描述的结构是一个松散的结构，后期可以改进
        for index in range(len(postTitle)):
            item = CnblogsItem()
            item['title'] = postTitle[index].css("a").xpath('text()').extract()[0]
            #print item['title'] + "***************\r\n"
            item['link'] = postTitle[index].css('a').xpath('@href').extract()[0]
            item['listUrl'] = base_url
            item['desc'] = postCon[index].xpath('text()').extract()[0]
            #print base_url + "********\n"
            items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'
        return items