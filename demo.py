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
import random
reload(sys)
sys.setdefaultencoding('utf-8')



def test(max_time):
    max_behost_time =str(time.time())[0:12]
    max_create_time= float(str(time.time())[0:12])+552
    max_time=float(str(time.time())[0:12])+1162
    htmlUrl = 'http://toutiao.com/api/article/recent/?source=2&count=20&category=__all__&max_behot_time=1457780334.83&utm_source=toutiao&offset=0&_=%s'%max_time
    # htmlUrl = 'http://toutiao.com/api/article/recent/?source=2&count=20&category=__all__&'+ 'max_behot_time=%s'%(max_behost_time)+'&utm_source=toutiao&offset=0&' \
    # 'max_create_time=%s'%max_create_time+'&_=%s'%max_time
    #


    html = requests.get(htmlUrl).content
    send_headers = {
    'Host': 'm.toutiao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive',}
    req = urllib2.Request(htmlUrl, headers=send_headers)


    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req)
    print

    print 'Spider is working...........'

    with open('toutiao.json', 'w') as myfle:
       # myfle.write(response.read().decode('gbk'))
       myfle.write(response.read().decode(encoding='utf-8'))
       # 解析jSON文件
    with open('toutiao.json', 'r') as myfle:
      text = json.load(myfle, encoding='utf-8')
    # print text
    # print text['message']#读取文件
    # print text['data'][0]['abstract']
    # print len(text['data'])

    for i in range(len(text['data'])):
          print '%s' % i + text['data'][i]['abstract'] + '\n'
          print text['data'][i]['datetime']+'\n'
    #


    print  htmlUrl
    print 'Spider is finished......'


if __name__ == '__main__':
     max_time=1457780334962
     while True:
       test(max_time)
       max_time += 1
=======
import urllib2
import cookielib
import urllib
import re
import sys
import requests


'''模拟登录'''
reload(sys)
sys.setdefaultencoding("utf-8")
# 防止中文报错
CaptchaUrl = "http://jwc2.usst.edu.cn/CheckCode.aspx"
PostUrl = "http://jwc2.usst.edu.cn/"
# 验证码地址和post地址
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)


filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)




# 将cookies绑定到一个opener cookie由cookielib自动管理
username = '1219010716'
password = 'LBQ123456789'
# 用户名和密码
picture = opener.open(CaptchaUrl).read()
# 用openr访问验证码地址,获取cookie
local = open('image.jpg', 'wb')
local.write(picture)
local.close()
# 保存验证码到本地
SecretCode = raw_input('输入验证码： ')
# 打开保存的验证码图片 输入
postData = {
    '__VIEWSTATE': '/wEPDwUKLTMzMTEwODcxMGRkJAW6cpghkvjOU6N9cEOW+hpudZY=',
    'TextBox1': username,
    'TextBox2': password,
    'TextBox3': SecretCode,
    'RadioButtonList1': '学生',
    'Button1': '',
    'lbLanguage': '',
    '__EVENTVALIDATION': '/wEWDAKlpsy3CALs0bLrBgLs0fbZDALs0Yq1BQK/wuqQDgKAqenNDQLN7c0VAuaMg+'
                         'INAveMotMNAoznisYGArursYYIAt+RzN8IfxS41dvoQASn4ntp6uE84yEfw/o=',

}
# 根据抓包信息 构造表单
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded',
    'Host':'jwc1.usst.edu.cn',
    'Origin':'http://jwc2.usst.edu.cn',
    'Referer':'http://jwc2.usst.edu.cn/',
    # 'Cookie':'ASP.NET_SessionId=s2!!2q0fd455cdihfsjjavoo2z45',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}
# 根据抓包信息 构造headers
data = urllib.urlencode(postData)
# 生成post数据 ?key1=value1&key2=value2的形式
request = urllib2.Request(PostUrl, data, headers)
# 构造request请求
''''''






try:
   response = opener.open(request)
   gradeUrl = 'http://jwc2.usst.edu.cn/xscjjdb.aspx?xh=1219010716&xm=%C1%D6%B1%FE%C7%BF&gnmkdm=N121621'

   result = response.read().decode('gb2312')
   # 由于该网页是gb2312的编码，所以需要解码
   print result
   #start

   # filename = 'cookie.txt'
   # #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
   # cookie = cookielib.MozillaCookieJar(filename)
   # #保存cookie到cookie.txt中
   # cookie.save(ignore_discard=True, ignore_expires=True)
   gradeUrl = 'http://jwc2.usst.edu.cn/xscjjdb.aspx?xh=1219010716&xm=%C1%D6%B1%FE%C7%BF&gnmkdm=N121621'

   #请求访问成绩查询网址
   result = open(gradeUrl)
   print result.read().decode('gb2312')
   #end

   # with open('school.html','wb') as myfile:
   #     myfile.write(result)
   # class_url = 'http://jwc2.usst.edu.cn/xs_main.aspx?xh=1219010716'
   # session =  requests.session()
   # html = session.post(class_url,data)
   # print html


except urllib2.HTTPError, e:
   print e.code
   # 利用之前存有cookie的opener登录页面
>>>>>>> c955e0e83d06cd5ba576c34d00216e5bf3bdbbea
