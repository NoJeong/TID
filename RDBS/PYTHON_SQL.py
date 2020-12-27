import pymysql
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='a1800710', db='ecommerce', charset='utf8')
db
#Cursor Object 가져오기: cursor = db.cursor()
ecommerce = db.cursor()
ecommerce

sql = """
    CREATE TABLE product (
        PRODUCT_CODE VARCHAR(20) NOT NULL,
        TITLE VARCHAR(200) NOT NULL,
        ORI_PRICE INT,
        DISCOUNT_PRICE INT,
        DISCOUNT_PERCENT INT,
        DELIVERY VARCHAR(2),
        PRIMARY KEY(PRODUCT_CODE)
    );
"""

#SQL 실행하기: cursor.execute(SQL)
ecommerce.execute(sql)

db.commit()

db.close()


######################
#pattern

# 1. 라이브러리 가져오기
import pymysql

# 2. 접속하기
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='a1817263', db='ecommerce', charset='utf8')

# 3. 커서 가져오기
cursor = db.cursor()

# 4. SQL 구문 만들기 (CRUD SQL 구문 등)
sql = '''
    CREATE TABLE product (
        PRODUCT_CODE VARCHAR(20) NOT NULL,
        TITLE VARCHAR(200) NOT NULL,
        ORI_PRICE INT,
        DISCOUNT_PRICE INT,
        DISCOUNT_PERCENT INT,
        DELIVERY VARCHAR(2),
        PRIMARY KEY(PRODUCT_CODE)
    );
'''

# 5. SQL 구문 실행하기
cursor.execute(sql)

# 6. DB에 Complete 하기
db.commit()

# 7. DB 연결 닫기
db.close()

#########################
# 데이터 삽입
import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='a1800710', db='ecommerce', charset='utf8')

cursor = db.cursor()

for index in range(10):
    product_code = 215673140 + index + 1
    sql = """INSERT INTO product VALUES(
    '""" + str(product_code) + """', '스위트바니 여름신상5900원~롱원피스티셔츠/긴팔/반팔', 23000, 6900, 70, 'F'); """
    print (sql)
    cursor.execute(sql)

db.commit()
db.close()

########################
#데이터 조회
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='a1800710', db='ecommerce', charset='utf8')
cursor = db.cursor()
sql = "SELECT * FROM product"
cursor.execute(sql)
result = cursor.fetchmany(size=5)
print(result)
result = cursor.fetchone()
print(result)
result = cursor.fetchall()
print(result)

db.close()
############################
#데이터 수정

# 1. 라이브러리 가져오기
import pymysql

# 2. 접속하기
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='a1800710', db='ecommerce', charset='utf8')

# 3. 커서 가져오기
cursor = db.cursor()

# 4. SQL 구문 만들기
SQL = """
UPDATE product SET 
    TITLE='달리샵린넨원피스 뷔스티에 썸머 가디건 코디전', 
    ORI_PRICE=33000, 
    DISCOUNT_PRICE=9900, 
    DISCOUNT_PERCENT=70 
    WHERE PRODUCT_CODE='215673141'
"""

# 5. SQL 구문 실행하기
cursor.execute(SQL)

# 6. commit 하기
db.commit()

# 7. close 하기
db.close()

########################################
# 데이터 삭제
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='a1800710', db='ecommerce', charset='utf8')

cursor = db.cursor()

SQL = """DELETE FROM product WHERE PRODUCT_CODE='215673142'"""

cursor.execute(SQL)

db.commit()

db.close()