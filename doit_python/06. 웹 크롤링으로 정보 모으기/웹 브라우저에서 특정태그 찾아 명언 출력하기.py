import re,usercsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs


url = 'https://quotes.toscrape.com/'

soup = bs(ur.urlopen(url).read(),'html.parser')

soup.find_all('span')

quote = soup.find_all('span')

# div태그 안에 정의된 특정 클래스를 찾아가는법
#div의 클래스는 quote

soup.find_all('div',{'class':"quote"})
print(soup.find_all('div',{'class':"quote"})[0])

# 이안에서 텍스트만 출력하기
soup.find_all('div',{'class':"quote"})[0].text
print(soup.find_all('div',{'class':"quote"})[0].text)

# 반복문으로 모든 명언 출력하기
for i in soup.find_all('div',{'class':"quote"}):
    i.text
    print(i.text)