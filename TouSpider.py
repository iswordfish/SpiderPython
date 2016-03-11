#coding:utf-8
'''
今日头条爬去
'''

import requests
import re
from bs4 import BeautifulSoup
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


htmlUrl = 'http://m.toutiao.com/list/?tag=__all__&ac=wap&item_type=4&count=20&format=json&list_data_v2=' \
          '1&max_behot_time=1457687832&ad_pos=4&ad_gap=6&csrfmiddlewaretoken=f7e8988c3e1ed50138a7d047404930d3'


htmlJs_Url = 'http://toutiao.com/api/article/recent/?source=2&count=20&category=' \
             '__all__&max_behot_time=1457602461.21&utm_source=toutiao&offset=0&_=1457602461239'


html = requests.get(htmlUrl).content
print 'Spider is working...........'
demo_data = html
# data = dict(demo_data)
# print type(html)
# print len(html)

with open('toutiao.json','w') as myfle:
    myfle.write(html)
#解析jSON文件


with open('toutiao.json','r') as myfle:
    text = json.load(myfle,encoding='utf-8',)
    # print text
    # print text['message']#读取文件
    # print text['data'][0]['abstract']
    # print len(text['data'])
    for i in range(len(text['data'])):
        print '%s'%i + text['data'][i]['abstract']+'\n'
print 'Spider is finished......'