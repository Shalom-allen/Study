import pandas as pd
from google_play_scraper import Sort, reviews

total_reviews = []
count_per_request = 100  # 한 번에 가져올 리뷰 수
target_count = 500  # 목표 리뷰 수500

result, continuation_token = reviews(
    'com.laundrygo.android', #요기에 가지고오고싶은 어플의 주소와
    lang='ko',  #한국어
    country='kr',  # 한국이고
    sort=Sort.NEWEST, #최근꺼 순으로
    count=count_per_request,
)

total_reviews.extend(result)

while len(total_reviews) < target_count and continuation_token: #이걸로 인해서 100,100,100,100,100 이런식으로 가지고 오려고하는거다.
    result, continuation_token = reviews(
        'com.laundrygo.android',
        lang='ko',
        country='kr',
        sort=Sort.NEWEST,
        count=count_per_request,
        continuation_token=continuation_token
    )
    total_reviews.extend(result)

# 데이터프레임으로 변환
playstore_reviews_df = pd.DataFrame(total_reviews[:target_count])

#print(playstore_reviews_df)
playstore_reviews_df.to_excel("test.xlsx", index=False, engine='openpyxl')