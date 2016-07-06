# -*- coding: utf-8 -*-
'''
网络爬虫之用户名密码及验证码登陆：爬取知乎网站
'''
import requests
import re
import time
from bs4 import BeautifulSoup

LOGIN_URL_POST='http://www.zhihu.com/login/email'
LOGIN_URL = 'http://www.zhihu.com/#signin'
USERNAME = '1848406889@qq.com'
PASSWORD = 'LBQ139196'
filname='login.html'

HEADERS ={
     'Accept':'*/*' ,
     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
     'X-Requested-With':'XMLHttpRequest',
     'Referer':'http://www.zhihu.com',
     'Accept-Language':'zh-CN',
     'Accept-Encoding':'gzip, deflate',
     'User-Agent':'Mozilla/5.0(Windows NT 6.1;WOW64;Trident/7.0;rv:11.0)like Gecko',
     'Host':'www.zhihu.com'
     }
FORM_DATA = {
    'password': PASSWORD,
    'email': USERNAME,
    'remeber_me': 'true',
    'captcha': '1222',

}
'''
'captcha':'1222',
    '_xsrf':'xsrf',

    '''

'''将登陆页面下载到本地查找验证码'''
s = requests.Session()
html = s.get(LOGIN_URL,headers=HEADERS)
content = html.content



with open(filname, 'w') as f:
    f.write(content)



html=open(filname,'r')
soup=BeautifulSoup(html, "html.parser")
xsrf=soup.find('input',{'name':'_xsrf'})['value']
print '_xsrf:{0}'.format(xsrf)

print(str(int(time.time()*1000)))
Captcha_URL= 'http://www.zhihu.com/captcha.gif?r='+ str(int(time.time()*1000))
r = s.get(Captcha_URL,headers =HEADERS)

with open('captcha.jpg','w') as f:
    f.write(r.content)


captcha =raw_input('captcha: ')
login_data ={
    '_xsrf':xsrf,
    'email':USERNAME,
    'password':PASSWORD,
    'remember_me':'true',
    'captcha':captcha
    }




import  pickle

def save_cookies(requests_cookiejar, filename):
    with open('cookies.txt', 'wb') as f:
        pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)




reLogin=s.post(LOGIN_URL_POST,data=login_data,headers=HEADERS)


save_cookies(reLogin.cookies, 'cookies.txt')


print reLogin.status_code
r =s.get('http://www.zhihu.com',cookies=load_cookies('cookies.txt'),headers=HEADERS)
print(r.text)













#
# def getXsrf(filname):
#         html=open(filname,'r')
#         soup=BeautifulSoup(html, "html.parser")
#         xsrf=soup.find('input',{'name':'_xsrf'})['value']
#         print '_xsrf:{0}'.format(xsrf)



