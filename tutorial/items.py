# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


import scrapy

class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


from scrapy.item import Item, Field


class ZhihuItem(Item):
    url = Field()  #保存抓取问题的url
    title = Field()  #抓取问题的标题
    description = Field()  #抓取问题的描述
    answer = Field()  #抓取问题的答案
    name = Field()  #个人用户的名称


class CnblogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    listUrl = scrapy.Field()

class Website(Item):

    name = Field()
    description = Field()
    url = Field()


class SgfPython(Item):
    title = Field()
    # link = Field()

class BobaoItem(scrapy.Item):
    name=scrapy.Field() #文章名
    link=scrapy.Field() #链接
    time=scrapy.Field() #发布时间

