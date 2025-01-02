import requests
from bs4 import BeautifulSoup

# 네이버 카페 URL (예: Granado Espada 게시판)
url = 'https://cafe.naver.com/granadoespadam'

# 웹페이지 요청
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)
response.raise_for_status()

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 게시글 제목 추출
titles = soup.select('a.article')

# 게시글 제목 출력
for title in titles:
    print(title.text.strip())
