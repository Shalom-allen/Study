# 패키지 설치
import pandas as pd
import pickle
import MySQLdb as mydb
import sys
import requests
from bs4 import BeautifulSoup

# 멜론 차트 가져오기
if __name__ == "__main__":
    RANK = 100
    
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')
    titles = parse.find_all("div", {"class": "ellipsis rank01"})
    singers = parse.find_all("div", {"class": "ellipsis rank02"})

    title = []
    singer = []

    for t in titles:
        title.append(t.find('a').text)

    for s in singers:
        singer.append(s.find('span', {"class": "checkEllipsis"}).text)
    items = [item for item in zip(title, singer)]

# DB 연결
conn = mydb.connect(
    user="root",
    passwd="123",
    host="localhost",
    db="ALLEN"
    , charset='utf8'
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
