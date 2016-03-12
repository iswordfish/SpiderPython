# coding:utf-8
'''
今日头条爬去
'''

import requests
import re
from bs4 import BeautifulSoup
import urllib2
import json
import sys
import urllib2
import urllib
import time

reload(sys)
sys.setdefaultencoding('utf-8')

htmlUrl = \
    'http://toutiao.com/api/article/recent/?source=2&count=20&category=__all__&max_behot_time=1457701871&utm_source=toutiao&offset=0&max_create_time=1457701900&_=1457700917099'

html = requests.get(htmlUrl).content
send_headers = {
    'Host': 'm.toutiao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive',

}
max_behost_time = float(str(time.time())[0:12])

post_data = {
    'source': '2',
    'count': '20',
    'category': '__all__',
    'max_behot_time': '1457699986.6',
    'utm_source': 'toutiao',
    'offset': '0',
    '_': '1457699985928',
}

req = urllib2.Request(htmlUrl, headers=send_headers)
data = urllib.urlencode(post_data)
# enable cookie
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
response = opener.open(req, data)
print

print 'Spider is working...........'

with open('toutiao.json', 'w') as myfle:
    myfle.write(response.read())
# 解析jSON文件
with open('toutiao.json', 'r') as myfle:
    text = json.load(myfle, encoding='utf-8', )
    # print text
    # print text['message']#读取文件
    # print text['data'][0]['abstract']
    # print len(text['data'])
    for i in range(len(text['data'])):
        print '%s' % i + text['data'][i]['abstract'] + '\n'

print 'Spider is finished......'
