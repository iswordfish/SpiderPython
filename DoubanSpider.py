# -*- encoding:utf-8 -*-
'''
针对有验证码的网站,模拟登陆可以先使用正确的用户和密码请求对login页码,
将页面下载下载下来,此时的cookie是和原先的一样的,然后输入验证码,将密码,用户名
和验证码重新发送便可以模拟登陆
'''

import requests
from bs4 import BeautifulSoup
import urllib
import re

username = '1848406889@qq.com'
password = 'LBQ139196'
username1 = '18818261892@163.com'
password1= 'LBQ139196'
loginUrl = 'https://accounts.douban.com/login'
redir="https://shanghai.douban.com/"


formData = {
    'source':'location',
    "redir": redir,
    "form_email": username,
    "form_password": password,
    "login": u'登录'
}



headers = {
    'Host':'www.douban.com',
    'Referer':'https://www.douban.com/',
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
session=requests.Session()
r=session.post(loginUrl, data=formData, headers=headers)
page = r.content
with open('login.html', 'w') as fp:
    fp.write(page)



html = open('login.html', 'r')
soup = BeautifulSoup(html, "html.parser")

captchaAddr = soup.find('img', id='captcha_image')['src']
# captchaAddr = soup.find_all('img',id='captcha_image')

reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'

captchaID = re.findall(reCaptchaID, page)

urllib.urlretrieve(captchaAddr, "captcha.jpg")
captcha = raw_input('please input the captcha:')

formData['captcha-solution'] = captcha
formData['captcha-id'] = captchaID

r=session.post(loginUrl, data=formData, headers=headers)


page = r.content
print r.url
# print r.content

import  pickle

def save_cookies(requests_cookiejar, filename):
    with open('cookies.txt', 'wb') as f:
        pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


save_cookies(r.cookies, 'cookies.txt')


'''
this is a test'''


if r.url == redir:
    print 'Login successfully!!!'
    print 'the movie', '-' * 60
    print r.status_code
    print r.cookies#OUTPUT:<RequestsCookieJar[<Cookie ck=AU0U for .douban.com/>, <Cookie ll="108296" for .douban.com/>]>

    # html = session.get('https://book.douban.com/',cookies=load_cookies('cookies.txt'),headers=headers)
    html = session.get('https://www.douban.com/people/141360318/',cookies=load_cookies('cookies.txt'),headers=headers)
    # print html.cookies#OUTPUT:<RequestsCookieJar[]>

    print html.content


else:
    print "failed!"


