import re,usercsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs


url = 'https://quotes.toscrape.com/'

soup = bs(ur.urlopen(url).read(),'html.parser')

# find_all 로 원하는 태그마 모으기
soup.find_all('span')
# print(soup.find_all('span'))

quote = soup.find_all('span')

print(quote[0])
# <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
print(quote[0].text)
# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”

#그럼 반복문을 이용해서 text클래스를 가진 span태그를 가져오쟈
for i in quote:
    i.text
    print(i.text)