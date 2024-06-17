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
cursor.execute("TRUNCATE TABLE melon")

# 테이블 생성하기
#cursor.execute("CREATE TABLE melon (`rank` int, title text, url text)")
i = 1
# 데이터 저장하기
for item in items:
    cursor.execute(
        f"INSERT INTO melon VALUES({i},\"{item[0]}\",\"{item[1]}\")")
    i += 1

# 커밋하기
conn.commit()
# 연결종료하기
conn.close()
