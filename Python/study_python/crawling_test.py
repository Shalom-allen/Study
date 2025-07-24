import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://audition.hanbiton.com/Community/TalkBoardList.aspx'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
session = requests.Session()

res = session.get(BASE_URL, headers=HEADERS)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup)
'''
def get_first_post_id():
    res = session.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    rows = soup.select('table.board_list tr')

    for i, row in enumerate(rows):
        # 공지인지 확인
        if row.select_one('img[src*="icon_notice.gif"]'):
            print(f"[{i}] 공지글 건너뜀")
            continue  # 공지글은 skip

        # 일반글에서 링크 추출
        link = row.select_one('td.subject a')
        if link:
            href = link.get('href', '')
            if 'idx=' in href:
                post_id = href.split('idx=')[-1]
                print(f"[{i}] 일반글 ID: {post_id}")
                return post_id
            else:
                print(f"[{i}] 'idx=' 포함 안됨: {href}")
        else:
            print(f"[{i}] 링크 없음")

    print("일반 게시글을 찾을 수 없습니다.")
    return None

def get_post_detail(post_id):
    post_url = f"https://audition.hanbiton.com/Community/TalkBoardView.aspx?BoardType=1&idx={post_id}"
    res = session.get(post_url, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select_one('.view_subject')
    content = soup.select_one('.view_text')
    info = soup.select('.view_info span')

    writer = info[0].text.replace('작성자 :', '').strip() if len(info) > 0 else ''
    date = info[1].text.replace('등록일 :', '').strip() if len(info) > 1 else ''

    comments = []
    for li in soup.select('.comment_list > ul > li'):
        c_writer = li.select_one('.comment_writer').text.strip()
        c_date = li.select_one('.comment_date').text.strip()
        c_content = li.select_one('.comment_text').text.strip()
        comments.append({
            '작성자': c_writer,
            '작성일자': c_date,
            '댓글': c_content
        })

    return {
        '게시글번호': post_id,
        '제목': title.text.strip() if title else '',
        '내용': content.text.strip() if content else '',
        '작성자': writer,
        '작성일자': date,
        '댓글': comments
    }


if __name__ == "__main__":
    post_id = get_first_post_id()
    if post_id:
        data = get_post_detail(post_id)
        print(data)
    else:
        print("게시글을 찾을 수 없습니다.")
'''