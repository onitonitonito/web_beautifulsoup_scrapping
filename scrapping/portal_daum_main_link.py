"""
#
#
"""
# root path 를 sys.path.insert 시키기 위한 코드 ... 최소 4줄 필요------------
import os, sys                                                          # 1
root_name = "web_beautifulsoup_scrapping"                               # 2
root = "".join(os.getcwd().partition(root_name)[:2])                    # 3
sys.path.insert(0, root)                                                # 4
# -------------------------------------------------------------------------

import re
import requests
import _assets.script_run

from bs4 import BeautifulSoup
from urllib.request import urlopen
from _assets.class_functions import (
                                    get_html_soup,
                                    get_finders,
                                    get_regex_extracts
                                    )

url_target = "http://www.daum.net"
regex_pattern = '(?<=href=").*?(?=")'

tags = ["a", { 'class' : 'link_favorsch'}]  # 인기 검색어
tags = ["a", { 'class' : 'link_txt'}]       # 주요기사

def main():
    html_soup = get_html_soup(url_target, getter=2)
    finders = get_finders(tags, html_soup)

    show_results_listed(finders, tags, detailed=0)
    show_results_listed(finders, tags, detailed=1)


def show_results_listed(finders, tags, detailed=False):
    print(f"find('{tags}') : {len(finders)}")
    print('-----------------'*4)
    for i, find in enumerate(finders, 1):
        text_string = find.text.replace('\n', '')
        href_string = get_regex_extracts(regex_pattern, str(find))

        if detailed:
            print(f"{i:>02}. {text_string}")
            print(f"  - {href_string}")
            print('-----------------'*4)
        else:
            print(f"   {i:>02}. {text_string}")

    print("\n")




if __name__ == '__main__':
    main()

# TODO: 각 분야별 주요뉴스 page 1/8 을 각각 불러서 저장하는 기능추가!
#       현재는 제일 첫번째 (default) 를 가져오는 것 만..
