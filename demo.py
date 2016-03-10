#coding:utf-8
'''
分页爬取糗事百科
页面跳转
爬去移动端直接爬去出现无法爬去的情况这时候需要添加Cookies


'''
import sys
from bs4 import BeautifulSoup
import urllib2
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')





cookie = {"Cookie":  '_qqq_uuid_="2|1:0|10:1456821975|10:_qqq_uuid_|56:Y2EwNmUyZThkYzc2MzgyMDZhZDNkNWI0MTVhMzNlMTMwNTVmNmEyNA==' \
         '|7259da0e627167a75a3b9f5bf323079c2a98ca4ad9847eba36f19e41b45cf8a7"; gr_user_id=577eb0e8-99f9-4252-bd49-7' \
         'f0b7f80b0de; _xsrf=2|619a8c69|07ad5b04532fd8bc8727e278073d85ab|1457575417; asp_furl=https%3A%2F%2Fwww.' \
         'baidu.com%2Flink%3Furl%3DqXFMXuXXkqFxWmk-ynhY83oeTtJnqPbqb3abU0Ctv3gYmFRvHy9mMJAwavq_YWn-%26wd%3D%26eqid' \
         '%3Dca8bd95f000456400000000256e0d5f8; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1456827392,1456832439,145683' \
         '2505,1457575423; ' \
         'Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1457576277; _ga=GA1.2.1542584989.1456821978; _gat=1'}

#初始化爬去的页面
pageNum = 0
#在爬去的每一张页面检查是否还有下一页这个字段
#如果有的话继续爬去剩余的页面
#如果没有的话停止爬去页面

#爬去页面的URL
htmlUrl = 'http://www.qiushibaike.com/8hr/page/'+('%s'%pageNum)+'/?s=4858587'
#下载对应的页面
htmlConten = requests.get(htmlUrl,cookies=cookie).content
#检查对应的页面有没有下一页这个字段
soup = BeautifulSoup(htmlConten,'html.parser')
wordNext = soup.find_all('span',attrs='next')
#还有下一页这个字段
if wordNext:
    print wordNext
    #TODO

