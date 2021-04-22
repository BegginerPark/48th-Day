import requests # 해당 사이트 불러 오기
from bs4 import BeautifulSoup # 시각화

url = "http://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html,"html5lib")
tags = soup.select("#_per") # 특정 태그만 표시
tags2 = soup.select("#_dvr")
tag = tags[0]
tag2 = tags2[0]
print(tag.text)
print(tag2.text)
