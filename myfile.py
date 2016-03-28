#coding:utf-8
import urllib2
#
# jpg_demo =  urllib2.urlopen('http://img3.fengniao.com/forum/attachpics/896/169/35833645_200.jpg')
# for i in range(1,10,1):
#     with open('%s'%i +".jpg",'wb') as myjpg:
#         myjpg.writelines(jpg_demo.read())
#     print('Pic Saved!')


for i  in range(1,10,1):
    with open('1.txt','a') as myfile:
           myfile.write(str(i))