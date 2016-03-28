#coding:utf-8
'''
爬去图片360好搜的图片
目标1000张
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

name =0
i=0
while i <=10000:
    htmlUrl = "http://image.so.com/zj?ch=wallpaper&sn=%s&listtype=hot"%(i+10)
    html = requests.get(htmlUrl).content
    send_headers = {
       'Host': 'm.toutiao.com',
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Connection': 'keep-alive', }
    max_behost_time = float(str(time.time())[0:12])

    post_data = {
          'source': '2',
         'count': '20',
         'category': '__all__',
        'max_behot_time': '1457699986.6',
       'utm_source': 'toutiao',
        'offset': '0',
        '_': '1457699985928',}

    req = urllib2.Request(htmlUrl, headers=send_headers)
    data = urllib.urlencode(post_data)
    # enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)


    print 'Spider is working...........'

    with open('toutiao.json', 'w') as myfle:
        myfle.write(response.read())
    # #添加链接
    # with open("url.txt","w") as myurl:
    #     myurl.write("demo"+'\n')
    # # 解析jSON文件
    with open('toutiao.json', 'r') as myfle:
        text = json.load(myfle, encoding='utf-8', )
    global name

    for i in range(len(text['list'])):
        print '%s' % i + text['list'][i]['cover_imgurl'] + '\n'
        myurl = text['list'][i]['cover_imgurl']
        with open('url.txt', 'a+') as myfle:
            myfle.write(myurl+'\n')
            #保存图片到本地
            print str(myurl)[0:-4]
        try:
           with open(str(name)+".jpg",'w') as myjpg:
              result = urllib2.urlopen(myurl)
              myjpg.write(result.read())
           name = name +1
           print "name"+str(name)
        except urllib2.URLError, e:
           print e.code





    print 'Spider is finished......'



