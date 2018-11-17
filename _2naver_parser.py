"""
# 네이버 첫페이지를 가져와 파싱하기
#
#
#"""
print(__doc__)

import urllib.request as req
from bs4 import BeautifulSoup

url = "http://www.naver.com/"
html = req.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
rank = soup.find("div")


print(type(rank))       # <class 'bs4.element.Tag'>


for i in rank.find_all("a", value=True, id=False):
    print(i)
    print(i.get_text(" ", strip=True))

# Tag 화일을 스트링화 해서 Write
with open(file='./_2naver_parser.html', mode='w', encoding='utf8') as f:
    f.write(str(rank))


"""
"""
