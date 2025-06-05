import folium
from geopy.geocoders import Nominatim
from IPython.display import display, HTML

# 맛집 목록
restaurants = [
    {"name": "한빛소프트", "address": "서울특별시 금천구 가산디지털1로 186, 제이플라츠 15층 1506호"}
]

# 위치 정보를 가져오기 위한 Geolocator 설정
geolocator = Nominatim(user_agent="geoapi")

# Folium 지도 생성 (가산디지털단지 중심)
map_ = folium.Map(location=[37.4773, 126.8873], zoom_start=15)

# 맛집 위치를 지도에 추가
for restaurant in restaurants:
    location = geolocator.geocode(restaurant["address"])
    if location:
        folium.Marker(
            [location.latitude, location.longitude],
            popup=f"{restaurant['name']}\n{restaurant['address']}"
        ).add_to(map_)

# 지도를 HTML로 변환하여 바로 표시
html_map = map_._repr_html_()
display(HTML(html_map))
