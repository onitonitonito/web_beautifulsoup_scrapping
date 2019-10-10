"""
# _2naver_parser.py - 네이버 첫페이지를 가져와 파싱하기
"""
# root path 를 sys.path.insert 시키기 위한 코드 ... 최소 4줄 필요------------
import os, sys                                                          # 1
root_name = "web_beautifulsoup_scrapping"                               # 2
root = "".join(os.getcwd().partition(root_name)[:2])                    # 3
sys.path.insert(0, root)                                                # 4
# -------------------------------------------------------------------------

import _assets.script_run

from bs4 import BeautifulSoup
from urllib.request import urlopen
from _assets.configs import join, dirs_dict
from _assets.class_functions import save_str_file

print(__doc__)

tags = ["div", ]
url_target = "http://www.naver.com/"
response = urlopen(url_target).read()
html_soup = BeautifulSoup(response, "html.parser")

rank = html_soup.find(tags)
print(type(rank))                       # <class 'bs4.element.Tag'>
print(rank.get_text(" ", strip=True))

finders = html_soup.find_all("a", value=True, id=False)
print(type(finders))                    # <class 'bs4.element.ResultSet'>
print(finders)                          # []

# Tag 화일을 스트링화 해서 Write ... txt형 화일로 생성 되었습니다..
string_data = str(rank)
filename_with_dir = join(dirs_dict['dir_results'], "_2naver_parser.html")
save_str_file(string_data, filename_with_dir)
