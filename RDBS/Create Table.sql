--탐색창 services.msc 검색
--mysql 실행된지 확인


--데이터 베이스 만들기
CREATE DATABASE mydata;

--데이터베이스 확인
SHOW DATABASES;

--DB 삭제
DROP DATABASE mydata;

--DB 삭제 ( 이름이 없어도 에러뜨지 X)
DROP DATABASE IF EXISTS mydata;

--어떤 DB 쓰겠다.
USE mydata;

-------------------------------------------------
--테이블 만들기
USE mydata;
CREATE TABLE myproduct (
	MYKEY INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRODUCTID TEXT NOT NULL,
    TITLE TEXT,
    ORI_PRICE INT,
    DISCOUNT_PRICE INT,
    DISCOUNT_PERCENT INT,
    DELEVERY TEXT,
    PRIMARY KEY(MYKEY)
);
SHOW TABLES;
DESC myproduct;

CREATE TABLE customer_db (
no INT NOT NULL AUTO_INCREMENT,
name CHAR(20) NOT NULL,
age TINYINT,
phone VARCHAR(20),
email VARCHAR(30) NOT NULL,
address VARCHAR(50),
PRIMARY KEY(no)
);
--테이블 구성 확인
DESC customer_db;
--테이블 삭제
DROP TABLE customer_db;

--테이블 컬럼 수정하는 방법
DESC customer_db;
ALTER TABLE customer_db ADD COLUMN model_type VARCHAR(10) NOT NULL;
DESC customer_db;
ALTER TABLE customer_db MODIFY COLUMN name VARCHAR(20) NOT NULL;
DESC customer_db;
ALTER TABLE customer_db CHANGE COLUMN name modelname VARCHAR(10);
DESC customer_db;
--컬럼 삭제방법
ALTER TABLE customer_db DROP COLUMN age;
DESC customer_db;