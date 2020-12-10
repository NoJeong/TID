import os, re, codecs
# 대본 받아오기
f = codecs.open('friends101.txt','r',encoding='utf-8')
script101 = f.read()
#확인해보기
print(script101[:100])


#특정 등장인물의 대사만 모으기

#'Monica:' 다음 아무 문자나 반복되는 패턴을 찾아서 리스트로 반환
Line = re.findall(r'Monica:.+', script101)

print(Line[:3])

for i in Line[:3]:
    print(i)


# 텍스트 파일로 저장
f = open('monica.txt','w',encoding='utf-8')

monica = ''
#monica 문자열에 하나씩 써보기

for i in Line:
    monica += i
#모니카에있는 문자열을 텍슽파일로 저장
f.write(monica)

#줄바꿈 적용해서 저장하기

monica = ''
for i in Line:
    monica += i + '\n'

f = open('monica.txt','w',encoding='utf-8')
f.write(monica)


#############################################################
#등장인물 리스트 만들기 

#대문자로 시작, 소문자 반복, 콜론형태
char = re.compile(r'[A-Z][a-z]+:')

a = re.findall(char, script101)
#중복 지우기
a = set(a)

# 끝에 콜론 지우기
a = list(a)
character = []
for i in a:
    character.append(i[:-1])

print(character)

# 이 명령어 한줄로 적어보기
character = [x[:-1] for x in list(set(re.findall(r'[A-Z][a-z]+:',script101)))]

print(character)
###################################################################

#지문만 출력하기 (등장인물이 어떻게 움직여야하는지)
r'\([A-Za-z].+[a-z|\.]\)'
# r' : 무조건 붙여주기
# \( : 괄호
#  [A-Za-z] : 괄호다음 공백없이 영문자가 온다
# .+ : 문자/숫자/빈칸 등이 자유롭게 반복된다
# [a-z|\.] : 마지막 글자로 영어 소문자 또는 마침표가 온다

a = re.findall(r'\([A-Za-z].+[a-z|\.]\)',script101)[:6]
print(a)

################################################################

#특정 단어의 예문만 모아서 파일로 저장하기

f = open('friends101.txt','r')
# f 안의 모든 문장을 원소로 하는 리스트를 만든다.
sentences = f.readlines()
#대사만 추출하기
for i in sentences[:20]:
    if re.match(r'[A-Z][a-z]+:', i):
        print(i)

#한줄로 만들어보기
lines = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i)]
print(lines[:10])

#대사중에 would 만 들어간 문장을 찾아보기 
would = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i) and re.search('would', i)]

print(would)

#대사중에 take 만 들어간 문장을 찾아보기 
take = [i for i in sentences if re.match(r'[A-Z][a-z]+:',i) and re.search('take', i)]

print(take)

# would 리스트 만들기
newf = open('would.txt','w')
#would리스트의 원소를 꺼내 한 줄씩 쓴다
newf.writelines(would)
