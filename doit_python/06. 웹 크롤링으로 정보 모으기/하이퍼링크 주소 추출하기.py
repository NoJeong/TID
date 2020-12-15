import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs


news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')

# a 태그만 추출하기
soup.find_all('a')
# print(soup.find_all('a'))

#href 속성값 추출하기

#a.get('속성')

#반복문으로 가져오기
for i in soup.find_all('a'):
    i.get('href')
    # print(i.get('href'))


#원하는 영역에서 하이퍼링크 모두 추출하기
#카드뉴스에서 a태그 추출
for i in soup.find_all('div', {"class": "item_issue"}):
    i.find_all('a')

#get으로 href 속성값 구하기
for i in soup.find_all('div', {"class": "item_issue"}):
    i.find_all('a')[0].get('href')
    print(i.find_all('a')[1].get('href'))