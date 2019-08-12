# from __future__ import print_function
"""
# B. 네이버 날씨 미세먼지 가져오기
# http://bit.ly/2YIcEXc
# ----
# 간단한 웹크롤링 따라하기
\n\n"""
print(__doc__)

import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url_target = 'https://search.naver.com/search.naver?query=날씨'

html = requests.get(url_target)
html.close()
# pprint(html.text)

soup = bs(html.text, 'html.parser')

# location = str(locations[0])[4:-5]
locations = soup.find('span', {'class': 'btn_select'}).findAll('em')
location = locations[0].text

data1 = soup.find('div', {'class': 'detail_box'})
# pprint(data1)

data2 = data1.findAll('dd')
# pprint(data2)


chemicals = [dat.find('span', {'class': 'num'}).text for dat in data2]
echo_messages = [
    f" WEB CRAWLING : NAVER WEATHER",
    f"-------------------------------",
    f" {location}",
    f"-------------------------------",
    f"  (1) PM 10   =  {chemicals[0]}",
    f"  (2) PM 2.5  =  {chemicals[1]}",
    f"  (3) O3 (Oz) =  {chemicals[2]}",
    f"-------------------------------",
]

[print(echo) for echo in echo_messages]
