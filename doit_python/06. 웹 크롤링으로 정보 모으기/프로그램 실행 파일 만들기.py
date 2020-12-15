import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs


news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')

f = open('links.txt','w')
#기사 링크를 파일로 저장하기
for i in soup.find_all('div',{'class':'item_issue'}):
    f.write(i.find_all('a')[0].get('href')+'\n')

#기사 본문을 파일로 저장하기
#원하는 기사 추출
article1 = 'https://sports.v.daum.net/v/20201215122516608'

soup2 = bs(ur.urlopen(article1).read(), 'html.parser')

f = open('article_1.txt','w')

for i in soup2.find_all('p'):
    f.write(i.text)


#기사 제목, 본문, 하이퍼링크 파일로 저장하기

f = open('article_total.txt','w')
for i in soup.find_all('div',{'class':'item_issue'}):
    try:
        #제목 쓰기
        f.write(i.text+'\n')
        #Url 주소를 쓰기
        f.write(i.find_all('a')[0].get('href') + '\n')
        #URL 주소 가져오기
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
        #p태그에서 본문만 추출하기 
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass
