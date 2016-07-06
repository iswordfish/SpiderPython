#coding:utf-8



import requests
from bs4 import BeautifulSoup

USERNAME = 'fizlbq@gmail.com'
PWD = 'Ll139196'

# LoginUrl = 'https://bitbucket.org/account/signin/'
LoginUrl = 'https://bitbucket.org/account/signin/'

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
    # 'csrfmiddlewaretoken': "csrfmiddlewaretoken",
    "username": USERNAME,
    "password": PWD,


}
s=requests.Session()
# RESULT = s.get(LoginUrl, headers=headers,data=formData)
RESULT = s.get(LoginUrl, headers=headers)
print

content = RESULT.content

with open('login.html', 'wb') as fp:
    fp.write(content)
html = open('login.html', 'r')
soup = BeautifulSoup(html, "html.parser")
token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

print token
formData['csrfmiddlewaretoken']=token




''' cooke'''
import  pickle

def save_cookies(requests_cookiejar, filename):
    with open('cookies.txt', 'wb') as f:
        pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


save_cookies(s.cookies, 'cookies.txt')







RESULT=s.post(LoginUrl, headers=headers,data=formData,cookies=load_cookies('cookies.txt'))
print RESULT.url


print RESULT.status_code
print RESULT.cookies

with open('test.html', 'w') as fp:
    fp.write(content)


html = open('test.html', 'r')
soup = BeautifulSoup(html, "html.parser")
token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
RESULT=s.post(LoginUrl, headers=headers,data=formData,)
print RESULT.status_code
print RESULT.cookies
print RESULT.content
