import time
import requests
import psycopg2
from psycopg2 import sql
from datetime import datetime

# PostgreSQL 접속 정보
DB_CONFIG = {
    'host': 'localhost',
    'dbname': 'study',
    'user': 'inserter',
    'password': '123qwe!!!',
    'port': 5432
}

import requests
from bs4 import BeautifulSoup


def fetch_bitcoin_price():
    url = 'https://www.google.com/finance/quote/BTC-USD?sa=X&ved=2ahUKEwjXqL6T1Zb-AhV9yDgGHX7qD5QQ3ecFegQINBAY'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        price_div = soup.find('div', {'class': 'YMlKec fxKbKc'})
        if price_div:
            return float(price_div.text.replace(',', '').strip())
        else:
            print("가격 정보를 찾을 수 없습니다.")
            return None
    except Exception as e:
        print(f"가격 조회 실패: {e}")
        return None


# 예시 실행
if __name__ == "__main__":
    price = fetch_bitcoin_price()
    if price:
        print(f"현재 비트코인 가격: ${price}")


# PostgreSQL에 데이터 삽입
def insert_price_to_db(price):
    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    sql.SQL("INSERT INTO tbl_bitcoin_price (price) VALUES (%s);"),
                    [price]
                )
        print(f"[{datetime.now()}] 삽입 성공: ${price}")
    except Exception as e:
        print(f"[{datetime.now()}] DB 삽입 실패: {e}")

# 무한 루프 실행
def main():
    while True:
        price = fetch_bitcoin_price()
        if price is not None:
            insert_price_to_db(price)
        time.sleep(10)  # 10초마다 반복

if __name__ == "__main__":
    main()
