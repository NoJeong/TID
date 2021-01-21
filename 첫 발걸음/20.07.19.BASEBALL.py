import pandas as pd

url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'

table = pd.read_html(url) #테이블을 가져오는 기능

#len(table) #테이블 갯수를 알아보는 기능 
print(table[0])

