#coding:utf8
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request
from scrapy.selector import Selector
from tutorial.items import  *
from scrapy import log
class SgfSpider(CrawlSpider):
    name = 'sgf'
    allowed_domains = ['segmentfault.com']
    login_page = 'https://segmentfault.com/api/user/login?_=1ba046f2112b0888153012b7768af83d'
    start_urls = ['https://segmentfault.com/t/python',]
    rules = (
        Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
             callback='parse_item', follow=True),
    )
    def __init__(self, *args, **kwargs):
        super(SgfSpider, self).__init__(*args, **kwargs)
        self.http_user = '18818261892@163.com'
        self.http_pass = 'LBQ139196'
        #login form

        self.formdata = {
                        'mail':self.http_user, \
                        'password':self.http_pass,\
                        }
        self.headers = {'ccept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',\
                        'Accept-Encoding':'gzip,deflate',\
                        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',\
                        'Connection':'keep-alive',\
                        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
                        }

    def init_request(self):
        """This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)


    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url, meta = {'cookiejar': i},\
                                formdata = self.formdata,\
                                headers = self.headers,\
                                callback = self.login)#jump to login page

    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'name': 'herman', 'password': 'password'},
                    callback=self.check_login_response)
    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if "Hi Herman" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            self.initialized()
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.
    def parse_item(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items


