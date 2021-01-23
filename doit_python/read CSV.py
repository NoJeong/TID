import csv
f = open('a.csv','r',encoding='utf-8-sig')
new = csv.reader(f)
# for i in new:
#     print(i)

#csv파일을 파이썬에서 사용할 수 있게 csv형 리스트로 바꾸기
a_list=[]
for i in new:
    # print(i)
    a_list.append(i)

# print(a_list)

#이걸 함수로 만들기

def opencsv(filename):
    f= open(filename,'r')
    reader = csv.reader(f)
    output=[]
    for i in reader:
        output.append(i)
    return output

# print(opencsv('example2.csv'))

# csv 파일 쓰기

a =[['구','전체','내국인','외국인'],
['관악구',519864,502089,17775],
['강남구',547602,542598,5104],
['송파구',686181,679247,6934],
['강동구',428547,424235,4312]]

f = open('abc.csv','w',newline='')
csvobject = csv.writer(f,delimiter=',')

csvobject.writerows(a)
# print(type(a),a)

# 이걸 함수화 하기

def writecsv(filename, the_list):
    f = open(filename,'w',newline='')
    a =csv.writer(f,delimiter=',')
    a.writerows(the_list)


#함수 임포트 해서 쓰기
import usercsv

a = [['국어','영어','수학'],[99,88,77]]
usercsv.writecsv('test.csv',a)


##########################################
#csv파일 안의 문자를 숫자로 전환하기

total =usercsv.opencsv('popSeoul.csv')

for i in total[:5]:
    # print(i)
    pass

#쉼표있는 숫자 int형으로 만들기
import re

j ='1,456,234'
a = float(re.sub(',','',j))
# print(a)

# csv파일의 숫자를 바꿔보기
i = total[2]
# print(i)
k =[]
for j in i:
    if re.search('\d',j):
        k.append(float(re.sub(',','',j)))

    else:
        k.append(j)

# print(,'I')

#숫자가 섞인 원소가있다면??

p =['123강남','123,546','11,886','76,465']
k = []
for i in p:
    if re.search('[a-z가-힣]',i):
        k.append(i)
    else:
        k.append(float(re.sub(',','',i)))

# print(k)

#특수문자가 섞여있다면??

i=['123!!','456,875','11,678','27,456']
k =[]
for j in i:
    if re.search('[a-z가-힣!]',j):
         k.append(j)
    else:
        k.append(float(re.sub(',','',j)))

# print(k)


#예외처리하기

i = ['123!!','345,345','11,678','43533','','!!*@#']

for j in i:
    try:
        i[i.index(j)]= float(re.sub(',','',j))
    except:
        pass
print(i)

#예외처리를 함수화 하기

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)]= float(re.sub(',','',j))
            except:
                pass
    return listName


#########################################
#외국인비율이 3%가 넘는 곳 구하기

#파일 불러오고 숫자형으로 바꾸기
total =usercsv.opencsv('popSeoul.csv')
newPop = usercsv.switch(total)
# print(newPop[0])

i = newPop[1]
foreign = round(i[2]/(i[1]+i[2]) * 100,1)
# print(foreign)

#외국인 비율 출력하기
for i in newPop:
    foreign = 0
    try:
        foreign = round(i[2]/(i[1]+i[2]) * 100,1)
        # print(i[0],foreign)
    except:
        pass

# 첫 행지정하기 
new=[['구','한국인','외국인','외국인비율(%)']]

# new.append([i[0],i[1],i[2],foreign])

# print(new)


#외국인 비율이 3%가 넘는 곳만 출력

for i in newPop:
    foreign =0
    try:
        foreign = round(i[2]/(i[1]+i[2]) * 100,1)
        if foreign > 3:
            # print([i[0],i[1],i[2],foreign])
            new.append([i[0],i[1],i[2],foreign])
    except:
        pass

usercsv.writecsv('newPop.csv',new)