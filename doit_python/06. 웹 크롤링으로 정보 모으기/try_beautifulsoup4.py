import re,usercsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

## 웹문서 자료를 가져와 가공하기

#urlopen으로 웹사이트 정보 가져오기

url = 'https://quotes.toscrape.com/'

# urllib.request.urlopen(url)

html = ur.urlopen(url)

print(html.read()[:100])
#뷰티풀 수프로 자료형 변환하기
soup = bs(html.read(), 'html.parser')
print(soup)
print(type(html)) # <class 'http.client.HTTPResponse'>
print(type(soup)) # <class 'bs4.BeautifulSoup'>

#이과정을 한줄로 표현하기
soup = bs(ur.urlopen(url).read(),'html.parser')

