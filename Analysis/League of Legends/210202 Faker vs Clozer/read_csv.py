import csv
f = open('../raw DATA/210131MID.csv', 'r', encoding='utf-8-sig')
new = csv.reader(f)
# for i in new:
#     print(i)

#csv 파일을 파이썬에서 사용할 수 있게 csv형 리스트로 바꾸기
array = []
for i in new:
    array.append(i)

print(array)

#숫자를 int형으로 만들기
import re

#예외처리를 함수화 하기
def switch(listName):
    for i in listName:
        for j in i:
            try:
                if re.search('\d',j):
                    i[i.index(j)]= float(re.sub(',','',j))
                
            except:
                pass
    return listName

result = switch(array)
# for i in result:
#     print(i)


final = []
for i in result:
    if i[0] == 'Name':
        continue
    temp = []
    for j in range(len(i)):
        if j == 0:
            temp.append(i[j])
        elif j == 7:
            temp.append(i[j])
    final.append(temp)
# print(final)
final_sorted = sorted(final, key=lambda x : -x[1])
# print(final_sorted)


final = []
for i in result:
    if i[0] == 'Name':
        print(i[21])
        continue
    temp = []
    for j in range(len(i)):
        if j == 0:
            temp.append(i[j])
        elif j == 21:
            temp.append(i[j])
    final.append(temp)
# print(final)
final_sorted = sorted(final, key=lambda x : -x[1])

for i in final_sorted:
    # print(i)
    pass