import requests
from bs4 import BeautifulSoup

# def get_per(code):
#     url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-" + code
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, "html5lib")
#     tags = soup.select("#_UpbitLayout > div:nth-child(4) > div > section.ty01 > article:nth-child(2) > div > span.marketB > div.up.ty01 > span.first > strong")
#     tag = tags[10]
#     return float(tag.text)

# def get_dividend(code):
#     url = "https://upbit.com/exchange?code=CRIX.UPBIT.KRW-" + code
#     html = requests.get(url).text
#     soup =BeautifulSoup(html,"html5lib")
#     tags = soup.select("#_")
#     tag = tags[0]
#     return float(tag.text)

def get_per(code):
    url = "https://www.bithumb.com"
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html5lib")
    tag = soup.select("#assetReal"+code+"_KRW")[0]
    

print(get_per("BTC"))
# print(get_dividend("BTC"))
print(get_per("ETH"))
# print(get_dividend("ETH"))



