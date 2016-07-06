#coding:utf-8
'''
https://bitbucket.org/account/signin/ 模拟登陆
'''


import requests
from bs4 import BeautifulSoup

USERNAME = 'fizlbq@gmail.com'
PWD = 'Ll139196'

LoginUrl = 'https://bitbucket.org/account/signin/'

user_url='https://bitbucket.org/fiz_LBQ/'


filename='login.html'

headers = {
    'Host': 'bitbucket.org',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://bitbucket.org/account/signin/?next=/',
    'Connection': 'keep-alive',
}

formData = {
    'next': '/',
    "username": USERNAME,
    "password": PWD,


}
s=requests.Session()
RESULT = s.get(LoginUrl, headers=headers)

content = RESULT.content

with open(filename, 'wb') as fp:
    fp.write(content)

html = open(filename, 'r')
soup = BeautifulSoup(html, "html.parser")
token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']



formData['csrfmiddlewaretoken']=token






RESULT=s.post(LoginUrl, headers=headers,data=formData,)
print RESULT.status_code
print RESULT.cookies
# print RESULT.content
''' 跳转到个人信息页面进行爬去'''
html_userInfo=s.get(user_url)


with open('bitbucket.html', 'w') as fp:
    fp.write(html_userInfo.content)