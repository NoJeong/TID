import numpy as np

a = np.array([[2,3],[5,2]])

# print(a)


d = np.array([[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]])


# print(d[1][2])
# #같음
# print(d[1, 2])
# #1행 2열부터의 값을 보여줌
# print(d[1:, 2:])

d = np.array([2,3,4,5,6])

# # 크기 알아보기
# print(d.shape)

e = np.array([[1,2,3,4],[3,4,5,6]])

# print(e.shape)


# #배열이 어떤 원소로 이루어져있는지
# print(d.dtype)


data = np.arange(1,5)
# print(data.dtype)

#배열 유형 바꾸기
a = data.astype('float64')
# print(a.dtype)

################################################

# # 0으로 이뤄진 배열 만들기
# print(np.zeros((2,10)))

# # 1으로 이뤄진 배열 만들기
# print(np.ones((2,10)))

# # 연속형 정수 생성하기 
# print(np.arange(2,10)) # 2 이상 10 미만의 원소로 이루어진 1차원의 배열을 만든다

# # 행과 열을 바꾸기 
# a = np.ones((2,3))
# b = np.transpose(a)
# print(b)

################################################
# 배열의 사칙연산

arr1 = np.array([[2,3,4],[6,7,8]])
arr2 = np.array([[12,23,34],[46,57,68]])
# #같은 자리끼리 더해짐
# print(arr1+arr2)
# #같은 자리끼리 곱해짐
# print(arr1*arr2)
# #같은 자리끼리 나눠짐
# print(arr1/arr2)


# 크기가 서로 다른 배열끼리 더하기

arr3 = np.array([100,200,300])

# print(arr1+arr3)

arr5 = np.array([[5],[3]])

# print(arr1+arr5)

#이경우에는 크기가 다르고 계산도 되지않는데 그 이유는 행과 열 둘중 하나의 값이 일치해야하기 떄문이다.
arr4 = np.array([100,200,300,400])

# print(arr1+arr4)

##########################################################
#리스트와의 차이점

d = np.array([[1,2,3,4,5],[2,4,5,6,7],[5,7,8,9,9]])
# print(d)
d[:2] = 0
# print(d)

#인덱싱과 슬라이싱

arr4 = np.arange(10)
# print(arr4[:5])
# print(arr4[-3:])
arr = np.array([[1,2,6],[3,4,5]])

# print(arr[1,2])

#모든 리스트의 세번째 원소를 슬라이싱하기
# print(arr[:,2])

####################################################
# 설문지 데이터 전처리하기

import usercsv
import numpy as np
#데이터 받아오기
quest = np.array(usercsv.switch(usercsv.opencsv('quest.csv')))

# print(quest)


#5보다 크면 True, 작거나 같으면 False
quest > 5
# print(quest > 5)

# 5보다 큰 수만 가져오기
quest[quest > 5]
# print(quest[quest > 5])

# 5보다 큰 점수를 5점ㅇ로 바꾸기
quest[quest > 5] = 5
# print(quest)


usercsv.writecsv('result.csv',list(quest))

##################################
# 넘파이로 사업성 분석하기 
import numpy as np

discount = .05 #할인율 0.05
cashflow = 100 #현금흐름 100

#현재가치를 구하는 공식을 함수로 만들기

def presentvalue(n):
    return (cashflow/ ((1 + discount) ** n))


# n년 후 현금흐름의 현재가치

# print(presentvalue(3))
# print(presentvalue(1))


#20년 동안 발생할 현재가치 모두 구하기 
for i in range(20):
    # print(presentvalue(i))
    pass
#######################################################
#놀이공원의 수익성 알아보기

#1,2년차에 발생한 비용
loss = [-750,-250]
#3년차부터 발생한 이익
profit = [100] * 18
#20년동안의 현금흐름을 리스트로 만들어서 cf에 저장했다.
cf = loss + profit
# print(cf)

cashflow = np.array(cf)

#순현재가치(NPV)와 내부수익률(IRR) 구하기

# #npv
# np.npv(할인율, 현금흐름)
# #irr
# np.irr(현금흐름)

# npv = np.npv(0.045,cashflow)
# print(npv)
# irr = np.irr(cashflow)
# print(irr)


#핵심지표 값 해석하기

#######################################
#판다스로 데이터프레임 만들기

import pandas as pd

data = { 'name': ['Mark','Jane','Chris','Ryan'],
    'age': [33,32,44,42],
    'score': [91.3, 83.4, 77.5, 87.7]}

df = pd.DataFrame(data)
# print(df)

#합계

# print(df.sum())

#평균

# print(df.mean())

#특정 데이터 선택하기 (df[key값] or df.key값)

# print(df.age)
# print(df['age'])


#########################
#csv파일 불러와 데이터프레임 만들기

#아파트 실거래가 정보를 살펴보기

import pandas as pd
import re, os

df = pd.read_csv('apt.csv',encoding='cp949')

print(len(df))

#처음이나 마지막 자료 일부만 출력하기
# print(df.head()) # 처음 다섯개
# print(df.tail()) #마지막 다섯개

#열 전체 자료 출력하기
# print(df.지역)

#조건별로 출력하기
# print(df.면적 > 130) #면적이 130이 넘으면 True 작거나 같으면 False

#해당 조건의 자료 전부를 보고싶다
# print(df[df.면적 > 130])

#이 조건의 가격만 보고싶다
# print(df.가격[df.면적 > 130])


#조건을 더 추가할 수 있다
#and
# print(df.가격[(df.면적 > 130) & (df.가격 < 15000)])
#or
# print(df.가격[(df.면적 > 130) | (df.가격 < 15000)])

#원하는 자료만 살펴보기
# df.loc[원하는 행의 조건, 원하는 열의 조건]

# print(df.loc[:10, ['아파트','가격']])

#여기에 조건 붙이기

# print(df.loc[:, ['아파트','가격']][df.가격 > 30000])

# 새로운 값 추가하기

#df['새로운 열 이름'] = 넣고싶은값

df['단가'] = df.가격 / df.면적
# print(df.loc[:10, ('가격', '면적', '단가')])

#데이터 정렬하기 
# df.sort_values(by='열이름') #오름차순
# df.sort_values(by='열이름', ascending=False) #내림차순

# print(df.sort_values(by='가격').loc[:, ('가격','지역')])
# print(df.sort_values(by='가격',ascending=False).loc[:, ('가격','지역')])

#4억이 넘는 아파트를 면적이 넓ㅅ어지는 순서로
# print(df[df.가격 > 40000].sort_values(by='면적').loc[:, ('가격','면적','지역')])

# 문자열 다루기
# 특정한 문자를 포함하는 열 추출(없다면 -1 반환)
# df.검색할열.str.find('찾는 문자열')
# print(df.지역.str.find('강릉'))
#다섯번째 문자에서 '강릉' 찾으면 4반환 없으면 -1

#'구미'가 들어간 자료만 부르기
# print(df[df.지역.str.find('구미') > -1])

# dfF = df[df.지역.str.find('구미') > -1]

# print(dfF.mean())

#만약 가격이 12,345 이런식으로 되어있다면 str타입으로 되어있는것이다. 그래서 ,를 제거해주고 float이나 int로 바꿔줘야한다
# df.가격 = df.가격.str.replace(',','').astype('int64')


##############################################
#판다스로 통계데이터 다루기

#기초 통계량 살펴보기
import pandas as pd
df2 = pd.read_csv('survey.csv')

# print(df2.head())

#평균과 합 구하기
# print(df2.mean())
# print(df2.income.mean())
# print(df2.income.sum())

# 중앙값 구하기
# print(df2.income.median())

#기초통계량 요약해서 출력하기
# print(df2.describe())
# print(df2.income.describe())

#기초통계량 분석하기
#빈도 분석하기
# df.변수.value_counts()

# print(df2.sex.value_counts())

#두 집단 평균 구하기
# df2.groupby(그룹을 나누는 변수).연산

print(df2.groupby(df2.sex).mean())

################################################################
#실전 통계분석 맛보기
from scipy import stats

male = df2.income[df2.sex == 'm']
female = df2.income[df2.sex == 'f']

print(stats.ttest_ind(male, female))

ttest_result = stats.ttest_ind(male,female)
print(ttest_result)

print(ttest_result[0]) #statistic
print(ttest_result[1]) #pvalue

if ttest_result[1] > .05:
    print('p-value는 {}로 95% 수준에서 유의하지 않음'.format(ttest_result[1]))
else:
    print('p-value는 {}로 95% 수준에서 유의함'.format(ttest_result[1]))


# 피어슨과 스피어만 상관관계 분석 알아보기

# df.corr() #피어슨 상관관계 분석 결과를 출력합니다
# df.corr(method = 'spearman') #스피어만 상관관계 분석 결과를 출력합니다

corr = df2.corr()
print(corr)
print(df2.corr(method='spearman'))


#수입과 스트레스의 상관관계만 보고싶다면
print(df2.income.corr(df2.stress))

#csv로 저장
corr.to_csv('corr.csv')

#statsmodels 패키지로 회귀분석하기

import statsmodels.formula.api as smf

# ols(formula='종속변수 ~ 독립변수', data = 데이터프레임)

model = smf.ols(formula = 'jobSatisfaction~English', data = df2)

result = model.fit()
print(result.summary())

#다중 회귀 분석 연습

# smf.ols(formula = '종속변수 ~ 독립변수1 + ... + 독립변수n', data = 데이터프레임)

model2 = smf.ols(formula = 'jobSatisfaction~English + stress + income', data = df2)
result = model2.fit()
print(result.summary())