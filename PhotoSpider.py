#coding:utf-8
'''
图片爬去
'''
import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
import random
import os


reload(sys)
sys.setdefaultencoding('utf-8')
image_url1 = 'http://bbs.fengniao.com/jinghua-18.html'
# html_content = requests.get(image_url1).content

html_img = urllib2.urlopen(image_url1)

html_content2 = html_img.read()

with open('images.html','w') as demoFile:

    for i in html_content2:

        demoFile.writelines(i)

soup = BeautifulSoup(html_content2, 'html.parser')




path=  os.getcwd()
if 'images' in os.listdir(path):
    os.chdir("images")
else:
    print False
    os.mkdir('images')
    os.chdir("images")
print  u'开始下载图片.........'
for link in soup.find_all('img'):
    #图片名称
    jpg_name = link.attrs['alt']

    #图片下载路径
    jgp_url = link.get('src')

    jpg_demo =  urllib2.urlopen(jgp_url)


    name = random.uniform(10, 200)

    path = os.getcwd()

    with open((str(jpg_name)+'.jpg'), "w") as myjpg:
        myjpg.writelines(jpg_demo.read())
        #("%s_imageurls"%user_id+'.txt'), "wb")
    print('Pic Saved in the'+' %s'% path)

print  u'图片下载完成'





