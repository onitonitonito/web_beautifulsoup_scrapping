"""
# 동아일보 키워드 뉴스서치 크로울링
# 결과정리 = 마크다운 목차(1폐이지만)
# 정리위치 = ./_statics/result/
#
"""
# print(__doc__)


import os

import lxml
import datetime
import urllib.request     # available?
# import requests         # temporary dimmed

from bs4 import BeautifulSoup
from urllib.parse import urlencode

KEY_WORD = '미세먼지&중국'

# 현재 화일이 있는 working dir.
# root_name = 'GDG_Air_incheon_BS4'
# dir_work = os.path.dirname(__file__)
#
# dir_works = dir_work.split('\\')
# while dir_works[-1] != root_name:
#     dir_works.pop()
#
# ROOT = "\\".join(dir_works)

# dir_static_result = os.path.join(ROOT, *['_statics', 'result',])
dir_static_result = os.path.join(*['_statics', 'result',])


url = 'http://news.donga.com/search'
param_dict = {
    'p' : '',
    'query' : KEY_WORD,
    'check_news' : '1',
    'more' : '1',
    'sorting' : '1',         # 정확도=3, 최신순=1
    'search_date' : '1',
    'v1' : '',
    'v2' : '',
    'range' : '3',
}

url_all = url + '?' + urlencode(query=param_dict)

source_code_from_url = urllib.request.urlopen(url_all)
soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')


# select 나 find_all 이나 결과는 똑같다. --> tag list 를 반환한다.
content_of_articles = soup.select('p.tit')
findings =  soup.find_all('p', 'tit')

search_md_string = f"## Search Result for '{KEY_WORD}'<br>\n"

for i, title in enumerate(soup.find_all('p', 'tit'),1):
    date_text = title.select('span')[-1].get_text()
    datetime_format = datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M')
    date_new = datetime.datetime.strftime(datetime_format, '%y.%m/%d(%a)')

    title_text = title.get_text().replace('\n', '').replace('  ', '').replace(date_text,'')

    title_link = title.select('a')
    article_URL = title_link[0]['href']

    print(f"{i:02}.[{date_new}] {title_text[:32]}..")
    search_md_string += f"{i:02}-[{date_new}] [{title_text}]({article_URL})\n"

search_md_string += "<br><br>\n"

file_name = f'{dir_static_result}/donga_result_{KEY_WORD}.md'
with open(file_name, mode='w', encoding='utf8') as f:
    f.write(search_md_string)



echo_messages = [
    f"  \n\n",
    f"-----------------------------------------------",
    f"* 동아일보 검색키워드 = '{KEY_WORD}' (1페이지)",
    f"* 검색결과 저장 위치  = .\\{dir_static_result}\\",
    f"* 저장된 화일 이름    = donga_result_{KEY_WORD}.md",
    f"  \n",
    f"마크다운의 하이퍼링크 목록을 확인 하세요 .. (Typora viewer)\n\n\n\n\n",
]

[print(message) for message in echo_messages]
