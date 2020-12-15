import re
import urllib.request as ur
from bs4 import BeautifulSoup as bs


news = 'https://news.daum.net/'

soup = bs(ur.urlopen(news).read(), 'html.parser')

print(soup)

