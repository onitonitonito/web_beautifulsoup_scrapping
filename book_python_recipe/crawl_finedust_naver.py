# from __future__ import print_function
"""
# B. 네이버 날씨 미세먼지 가져오기
# http://bit.ly/2YIcEXc
# ----
# 간단한 웹크롤링 따라하기
\n\n"""

# root path 를 sys.path.insert 시키기 위한 코드 ... 최소 4줄 필요------------
import os, sys                                                          # 1
root_name = "web_beautifulsoup_scrapping"                               # 2
root = "".join(os.getcwd().partition(root_name)[:2])                    # 3
sys.path.insert(0, root)                                                # 4
# -------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
from urllib.parse import (
                    urlparse,
                    urlunparse,
                    urlsplit,
                    urlunsplit,
                    urlencode,
                )

import _assets.script_run

print(__doc__)

url_target = 'https://search.naver.com/search.naver?query=날씨'
url_target = 'https://cafe.naver.com/joonggonara.cafe?iframe_url=/ArticleList.nhn?search.clubid=10050146&search.boardtype=L&viewType=pc'

"""
URLSPLIT =
# SplitResult( 5-tuples
#         scheme='https',
#         netloc='search.naver.com',
#         path='/search.naver',
#         query='query=날씨',
#         fragment='',
#     )

URLPARSE =
# ParseResult( 6-tuples ... add 'params'
#         scheme='https',
#         netloc='search.naver.com',
#         path='/search.naver',
#         params='',
#         query='query=날씨',
#         fragment='',
#     )
"""

# # FOR TEST!
# _ = urlsplit(url=url_target)
# # _ = urlparse(url=url_target
# _2 = urlsplit(url=_.query)
# print("1 = ",_)
# print("1q= ",_.query)
# print()
#
# print("2 = ",_2)
# print("2q= ",_2.query)
# quit()

param_dict = {
        'scheme'    : 'https',
        'netloc'    : 'search.naver.com',
        'path'      : '/search.naver',
        'params'    : '',
        'query'     : 'query=날씨',
        'fragment'  : '',
    }


url_base = "https://www.daum.net/q"
url = url_base + "?" + urlencode(query=param_dict)

html = requests.get(url_target)
html.close()
# print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

# location = str(locations[0])[4:-5]
locations = soup.find('span', {'class': 'btn_select'}).findAll('em')
location = locations[0].text

data1 = soup.find('div', {'class': 'detail_box'})
# print(data1)

data2 = data1.findAll('dd')
# print(data2)


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
