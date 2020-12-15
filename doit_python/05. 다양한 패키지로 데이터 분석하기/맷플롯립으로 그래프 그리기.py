import matplotlib.pyplot as plt


x = [1,4,9,16,25,36,49,64]
#그래프 생성하기
print(plt.plot(x))
plt.plot(x, color = 'r')
#그래프 보기
plt.show()

#축 이름 지정하기

y = [ i for i in range(1,9)]

plt.plot(x,y) #x,y그리기
plt.xlabel('x') #x축이름 설정
plt.ylabel('y') #y축이름 설정
plt.title('matplotlib sampe') #그래프 이름
plt.show()