 --터미널창에서 실시
 mysql -u root -p
 
 -- 사용자 확인  
 use  mysql;
 SELECT * FROM user;

 --사용자 추가
 use mysql

 -- 1) 로컬에서만 접속 가능한 userid 생성
 CREATE user 'userid'@localhost identified by '비밀번호';

 -- 2) 모든 호스트에서 접속 가능한 userid 생성
  CREATE user 'userid'@'%' identified by '비밀번호';

  -- 사용자 비밀번호 변경 
  SET PASSWORD FOR 'userid'@'%'='신규비밀번호';

  -- 사용자 삭제 
  use mysql
  DROP user 'userid'@'%';


  --------------------------------
  --mysql 접속 허용 관련 설정

  --현재 부여된 권한 확인하기
  SHOW GRANTS for '아이디';
  SHOW GRANTS for 'parkpark'@'%'

-- 1) 로컬에서만 접속허용
GRANT ALL ON ecommerce.product TO 'parkpark'@'localhost';

-- 2) 특정 호스트에서만 접속허용
GRANT ALL ON *.* TO 'parkpark'@'%';


-- 1) 모든 호스트에서 접속허용
GRANT SELECT, UPDATE ON *.* TO 'parkpark'@'%';