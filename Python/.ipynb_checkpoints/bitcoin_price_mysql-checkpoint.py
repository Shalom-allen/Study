import requests
from bs4 import BeautifulSoup
import MySQLdb as pymysql
import time

def get_bitcoin_price():
    url = "https://www.google.com/finance/quote/BTC-USD?hl=ko"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 비트코인 가격 정보 추출
    price_text = soup.find('div', {'class': 'YMlKec fxKbKc'}).text
    price = float(price_text.replace(',', '').replace('$', ''))
    return price

def insert_price(cursor, price):
    cursor.execute("INSERT INTO TBL_BITCOIN_PRICE (price) VALUES (%s)", (price,))

if __name__ == "__main__":
    conn = pymysql.connect(
        host='localhost'
        , user='root'
        , password='123'
        , db='ALLEN'
        , charset='utf8'
    )
    cursor = conn.cursor()

    while True:
        try:
            price = get_bitcoin_price()
            print(f"현재 가격: {price}")
            insert_price(cursor, price)
            conn.commit()
        except Exception as e:
            print(f"오류발생: {e}")

        # 10초 대기
        time.sleep(3)

    cursor.close()
    conn.close()