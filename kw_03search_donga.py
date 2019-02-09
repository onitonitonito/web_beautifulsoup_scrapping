"""
#
#
#
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

KEY_WORD = '미세먼지'

# 현재 화일이 있는 working dir.
root_name = 'web_beautifulsoup_scrapping'
dir_work = os.path.dirname(__file__)

dir_works = dir_work.split('\\')
while dir_works[-1] != root_name:
    dir_works.pop()

ROOT = "\\".join(dir_works)

dir_static_result = os.path.join(ROOT, *['static', 'result',])


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
