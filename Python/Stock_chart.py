# 패키지 설치
import pandas as pd
import MySQLdb as mydb
import requests
from bs4 import BeautifulSoup

# 코드 가져오기
code = '005930'
url = f'https://finance.naver.com/item/sise.naver?code={code}'
req = requests.get(url, header={'User-agent':'Mozilla/5.0'})
html = BeautifulSoup(req.text, "lxml")

# DB 연결
conn = mydb.connect(
    user="root",
    passwd="123",
    host="localhost",
    db="ALLEN", 
    harset='utf8'
)

# 커서 생성
cursor = conn.cursor()

# 실행할 때마다 다른값이 나오지 않게 테이블을 제거해두기
cursor.execute("TRUNCATE TABLE TBL_MELON_CHART")

# 테이블 생성
'''
CREATE or replace TABLE `TBL_MELON_CHART` (
  `rank` int(11) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `artist` varchar(100) DEFAULT NULL,
  `insert_date` datetime DEFAULT sysdate(),
  PRIMARY KEY (`rank`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
'''

# 데이터 저장하기
i = 1

for item in items:
    cursor.execute(
        f"INSERT INTO TBL_MELON_CHART(rank, title, artist) VALUES({i},\"{item[0]}\",\"{item[1]}\")")
    i += 1

# 커밋하기
conn.commit()
# 연결종료하기
conn.close()