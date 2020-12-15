import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs


news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')

soup.find_all('div',{'class':'item_issue'})
# print(soup.find_all('div',{'class':'item_issue'}))

#반복문으로 기사제목 추출하기
for i in soup.find_all('div',{'class':'item_issue'}):
    i.text
    print(i.text)