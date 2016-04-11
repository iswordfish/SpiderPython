#coding:utf-8
'''
健康界
'''
import requests
from bs4 import BeautifulSoup
import MySQLdb


Item ={'title':'default','link':'default','desc':'default','listUrl':'default'}
base_url ='http://www.cn-healthcare.com/'
count = 0
insert_count = 0


def demo(page=200):
    '''
    下载链接
    :param page:
    :return:
    '''
    global count
    try:
       base_url ='http://www.cn-healthcare.com/'
       post_url = r'api/article/articlelist?data={%22start%22:%223%22,%22size%22:%2210%22,%22arctype%22:%220%22}'
       url1 = 'api/article/articlelist?data={%22start%22:%'
       url3 =str(22)+ str(page)
       url2 = '%22,%22size%22:%2210%22,%22arctype%22:%220%22}'
       get_url = base_url+ url1+url3+url2
       response = requests.get(get_url).json()
       html = response
       # print base_url+(response.get('data'))[0]['url']
       # count +=1
       # print count
    except TypeError:
        print 'error'
    return base_url+(response.get('data'))[0]['url']


def choose_content(html):
    '''
    选取对应内容
    :param html:
    :return:
    '''
    soup = BeautifulSoup(html,"html.parser")
    try:
        title = soup.title.get_text()
        #新闻来源
        source = soup.find('span',attrs={'class':'wz-laiyuan'}).get_text()
         #发布时间
        produ_time = soup.find('span',attrs={'class':'wz-fbtime'}).get_text()
        #新闻主要内容
        content_n1 = soup.find_all('div',attrs={'class':'wz-textbox'})
        for i in content_n1:
             content_p = i.find('p').get_text()
             print content_p
        # print source
        # print produ_time
        return title,source,produ_time,content_p

    except AttributeError:
        print 'error'





if __name__ =='__main__':
    global insert_count
    for i in range(1,225):
        request_url = demo(page=i)
        result = requests.get(request_url).content
        # print result
        try:

            Item['title'],Item['link'],Item['desc'],Item['listUrl']=choose_content(result)[0],\
                                                                choose_content(result)[1],\
                                                                choose_content(result)[2],\
                                                                choose_content(result)[3],
            print Item

            try:
                   conn = MySQLdb.connect(host='localhost',user='root',passwd='1234',db='Blog',port=3306,charset='utf8',)
                   cur=conn.cursor()
                   cur.execute("""
                         insert into demo_cnblogsinfo( title, description, link, listUrl, updated)
                        values( %s, %s, %s, %s, %s)
                        """, ( Item['title'], Item['desc'], Item['link'], Item['listUrl'], 'list' ))
                   print 'insert OK111111111'
                   insert_count += 1
            #        cur.execute("""
            #     update demo_cnblogsinfo set title = %s, description = %s, link = %s, listUrl = %s, updated = %s where linkmd5id = %s
            # """, (Item['title'], Item['desc'], Item['link'], Item['listUrl'], str(datetime.now()), _get_linkmd5id(Item)))

                   # cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
                   cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
                   conn.commit()
                   cur.close()
                   conn.close()
                   print insert_count

            except MemoryError,e:
                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])

        except TypeError:
            Item['title'],Item['link'],Item['desc'],Item['listUrl']='0','0','0','0'
            print Item

            try:
                   conn = MySQLdb.connect(host='localhost',user='root',passwd='1234',db='Blog',port=3306,charset='utf8',)
                   cur=conn.cursor()
                   cur.execute("""
                         insert into demo_cnblogsinfo( title, description, link, listUrl, updated)
                        values( %s, %s, %s, %s, %s)
                        """, ( Item['title'], Item['desc'], Item['link'], Item['listUrl'],'list'  ))


                   conn.commit()
                   cur.close()
                   conn.close()
                   print insert_count

            except MemoryError,e:
                 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            print 'TypeError'







