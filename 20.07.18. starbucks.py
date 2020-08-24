import requests
from bs4 import BeautifulSoup

url = 'https://www.visitbusan.net/index.do?menuCd=DOM_000000201001000000'

response = requests.get(url).text

data = BeautifulSoup(response, 'html.parser')

k = data.find_all('p', 'tit')
for i in range(1,len(k)+1):
    select = data.select(f'#content > div > div.travel_list > div.trvList > div > div:nth-child({str(i)}) > div.info > p.tit > a')
    kkk = [k.text for k in select]
     #select로 할경우 리스트로 반환
     #[k.text for k in select]는 리스트에 있는 문자k에 대해서 k.text의 연산을 시행
     #k는 [k * 3 for k in select]는 각각의 k에게 3만큼 곱하는 이야기이다
    print(kkk)

q = data.find_all('p', 'tit')
for i in q:
    print(i.text)
    

#for i in range(1,5):
#    select3 = data.select_one(f'#content > div > div.travel_list > div.trvList > div > div:nth-of-type({str(i)}) > div.info > p.tit > a')
#    print(select3.text)
#print(select.text)