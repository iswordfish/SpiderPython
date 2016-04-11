# coding:utf-8
'''
模拟登陆拉勾网
https://passport.lagou.com/login/login.html
'''
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Host': 'passport.lagou.com',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
}

s = requests.session()
s.headers.update(headers)
login_url = r'https://passport.lagou.com/login/login.html'

html_url = s.get(login_url, headers=headers)
# print s.cookies.items()
# print "html_url code %s" % html_url.status_code
html_txt = html_url.text
print  html_txt

'''
TODO
'''




html_soup = BeautifulSoup(html_txt,'lxml')

img_soup = html_soup.find_all('img',class_="captcha_image")

# print img_soup

# for img_i in img_soup:
#     print img_i['src']
#     cap_img=img_i['src']
#
# for i in html_soup.find_all("input",attrs={"name":"captcha-id"}):
#     print i['value']
#     cap_i = i['value']
#
# captcha_solution=raw_input('输入验证码:')
# captcha_id=cap_i
# print captcha_solution
# print captcha_id
#
# url_data={
#     "source":"index_nav",
#     "form_email":"******",
#     "form_password":"******",
#     "captcha-solution":captcha_solution,
#     "captcha-id":captcha_id,
# }
#
# s_login=s.post(login_url,data=url_data,headers=headers)
#
# print s.cookies.items()
