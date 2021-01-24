#소비자 가격 = 물건가격 * 1.1
#물건가격 = 소비자 가격 * 1 / 1.1

# 8000원짜리 점심의 부가세는?

print(8000 * 0.1/1.1)
print(round(8000 /1.1,1))
print(round(8000 /1.1))
print(round(8000 * (1/11)))


y = lambda x : 3 * x

print(y(12))

add = lambda x, y : x + y
a = add(12,45)
print(a)

a = '나는 이제 오픽을 준비해야 한다.'

short = lambda x : x[:10]
print(short(a))


# 1원이 0.00086달러
exchange = lambda x : x * 0.00086
print(exchange(10000))

###############################i########################################################################################
# 가격 받아오기

price = {'a':23,'b':40,'c':72}



def service_price():
    service= input('서비스의 종류를 입력하세요, a,b,c: ')
    valueAdded = input('부가세를 포함합니까? y/n: ')
    if valueAdded == 'y':
        print(price[service] * 1.1)
    else:
        print(price[service])

service_price()