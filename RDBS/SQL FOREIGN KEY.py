import pymysql
import pandas as pd

host_name = 'localhost'
host_port = 3306
username = 'root'
password = 'a1800710'
database_name = 'sqlDB'

db = pymysql.connect(
    host=host_name,     # MySQL Server Address
    port=host_port,          # MySQL Server Port
    user=username,      # MySQL username
    passwd=password,    # password for MySQL username
    db=database_name,   # Database name
    charset='utf8'
)
#유저정보
SQL = "select * from userTbl"
df = pd.read_sql(SQL, db)
df
#구매 정보
SQL = "select * from buyTbl"
df = pd.read_sql(SQL, db)
df
#구매정보에 추가
cursor = db.cursor()
SQL_QUERY = "INSERT INTO buyTbl (userID, prodName, groupName, price, amount) VALUES('STJ', '운동화', '의류', 30, 2);"
cursor.execute(SQL_QUERY)
db.commit() # error 왜냐하면 외래키인 userID가 없어서

cursor = db.cursor()
SQL_QUERY = "INSERT INTO userTbl VALUES('STJ', '서태지', 1975, '경기', '011', '00000000', 171, '2014-4-4');"
cursor.execute(SQL_QUERY)
db.commit()

SQL_QUERY = "INSERT INTO buyTbl (userID, prodName, groupName, price, amount) VALUES('STJ', '운동화', '의류', 30, 2);"
cursor.execute(SQL_QUERY)
db.commit()

#삭제를 해보자 유저정보를
SQL_QUERY = "DELETE FROM userTbl WHERE userID = 'STJ'"
cursor.execute(SQL_QUERY)
db.commit()
#안된다 그이유는 외래키로 참조하고 있어서!
