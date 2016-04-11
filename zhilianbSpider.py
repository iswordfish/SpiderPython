# -*- coding: utf-8 -*-
'''
智联招聘登陆爬去自己的信息
'''
from urllib import urlencode
import cookielib, urllib2,urllib
def mylogin():
    headers={'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 5.1;zh-CN;rv:1.9.2.9)Gecko/20100824 Firefox/3.6.9'}
    post_dat = {'bkurl':'',
         'LoginName':'18818261892',
        'Password':'LBQ139196',
          'RememberMe':'true',}
    loginUrl = 'https://passport.zhaopin.com/account/login'
    data = urllib.urlencode(post_dat)
    cookiejar = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    urllib2.install_opener(opener)
    request = urllib2.Request(loginUrl ,data ,headers)
    result = urllib2.urlopen(request)
    login_result = result.read()
    if(login_result.find('.com/accounts/logout')):
        print 'login success'
        myurl2 = 'http://i.zhaopin.com/'
        scoreRequest=urllib2.Request(url=myurl2,)
        score=opener.open(scoreRequest)
        print score.read()


    else:
       print 'login faild'

if __name__  ==  '__main__':
     mylogin()