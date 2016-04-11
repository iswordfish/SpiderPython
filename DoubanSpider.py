# /usr/bin/python
#coding:utf-8
__author__ = 'eyu Fanne'

import requests
from bs4 import BeautifulSoup

headers={
    "Host":"www.douban.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
    "Connection":"keep-alive"
}

s=requests.session()
s.headers.update(headers)
login_url=r'https://www.douban.com/accounts/login'

html_url = s.get(login_url,headers=headers)
print s.cookies.items()
print "html_url code %s" %html_url.status_code
html_txt = html_url.text

html_soup = BeautifulSoup(html_txt,'lxml')

img_soup = html_soup.find_all('img',class_="captcha_image")

for img_i in img_soup:
    print img_i['src']
    cap_img=img_i['src']

for i in html_soup.find_all("input",attrs={"name":"captcha-id"}):
    print i['value']
    cap_i = i['value']

captcha_solution=raw_input('输入验证码:')
captcha_id=cap_i
print captcha_solution
print captcha_id

url_data={
    "source":"index_nav",
    "form_email":"******",
    "form_password":"******",
    "captcha-solution":captcha_solution,
    "captcha-id":captcha_id,
}

s_login=s.post(login_url,data=url_data,headers=headers)

print s.cookies.items()