import re, usercsv

apt = usercsv.switch(usercsv.opencsv('apt_202012.csv'))

# print(apt[0])

for i in apt[:6]:
    # #시군구 요소만 출력
    # print(i[0])
    # #단지명만 출력
    # print(i[4])
    # #거래금액만 출력
    # print(i[-4])
    pass
#강원도에 120m**2 이상 3억원 이하 아파트 검색하기
for i in apt:
    try:
        if i[5] > 120 and i[-4] >= 30000 and re.match('강원', i[0]):
            #시군구, 아파트단지명,가격출력
            print(i[0],i[4],i[-4])
    except:
        pass

#이 걸 csv에 저장하기

new_list = []

for i in apt:
    try:
        if i[5] > 120 and i[-4] >= 30000 and re.match('강원', i[0]):
            #시군구, 아파트단지명,가격출력
            new_list.append([i[0],i[4],i[-4]])
    except:
        pass

usercsv.writecsv('over120_over300.csv',new_list)