# mysql 테이블 생성



### mysql 초기시작

![mysql 초기 시작](C:%5CUsers%5Cop032%5CDesktop%5Cssafy%5CTID%5CmySQL_base%5Cmysql%20%EC%B4%88%EA%B8%B0%20%EC%8B%9C%EC%9E%91.PNG)

* 처음에는 mysql이 있는 폴더로 이동한다.
* `mysql -u<username> -p<password>`를 쓴다 여기서 `-p` 이후에 엔터치면 비밀번호를 대놓고 치지않아도 된다



### mysql 테이블 생성

* 중요부분 하이라이트 해놨다.

![mysql 테이블 생성](C:%5CUsers%5Cop032%5CDesktop%5Cssafy%5CTID%5CmySQL_base%5Cmysql%20%ED%85%8C%EC%9D%B4%EB%B8%94%20%EC%83%9D%EC%84%B1.PNG)

* 처음에는 database를 안만들고 시작해서 `No database selected` 라는 에러가 떴다.
* 그래서 다음과같이 database를 생성해줬다.
* table을 만들기 전에는 `use <database>`와 같이 database를 실행해줘야한다
* 그다음 table을 만든다 이때 `column명` 다음  `속성` 다음  `NULL or NOT NULL`  등 설정을해준다
* 그다음 보여주기를 한다