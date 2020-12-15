import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs


article1 = 'https://sports.v.daum.net/v/20201215122516608'

soup2 = bs(ur.urlopen(article1).read(), 'html.parser')

news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')
#기사는 p태그만 모으면 내용을 알 수 있다
for i in soup2.find_all('p'):
    print(i.text)

#기사 제목 가져오기
headline = soup.find_all('div',{'class':'item_issue'})
print(headline[0].text)


# 하이퍼 링크된 모든 기사의 제목과 본문 추출하기 
# 제목 for문으로 뽑아오기
for i in headline:
    print(i.text,'\n')
    #해당 기사가 올라와있는 웹사이트를 열어서 저장하기
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
    # 본문 추출하기
    for j in soup3.find_all('p'):
        print(j.text)