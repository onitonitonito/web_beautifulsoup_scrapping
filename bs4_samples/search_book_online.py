"""
# 교보문고 검색결과를 크롤링으로 보여 줌 -- by Ask Company
# 써치 키워드의 인코딩을 다소 어렵게 함 ... keyword_encode()
"""
# https://gist.github.com/allieus/2a083babf5a24bc10e7f5c9877473af5?fbclid=
# IwAR19rnMgVLeMi1-wp28hSMye685vRoSzcQMhp_qjX3WregAzQDmzZsqrj_U
# ----------------------
# TODO: 써치결과를 MD화일로 작성해서 WRITE 화일을 만듬
# TODO: 상위 3페이지의 결과를 마크다운으로 만들어 WRITE 해줌
import os, sys                                          # 1
root_name = "web_beautifulsoup_scrapping"               # 2
root = "".join(os.getcwd().partition(root_name)[:2])    # 3
sys.path.insert(0, root)                                # 4
import _assets.script_run

print(__doc__)

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from urllib.parse import urljoin

from _assets.configs import *
from _assets.class_functions import *

filename_with_dir = join(dirs_dict['dir_results'],
                        'book_search_result.md',
                        )

def main():
    _search_key = '리액트'
    _encoded = keyword_encode(_search_key)
    print(f'encode({_search_key}) = {_encoded}')   # &#54028;&#51060;&#50028;
    print('\n')


    book_info_md = search(_search_key)

    book_info_md_str = "\n".join(book_info_md)

    save_str_file(book_info_md_str, filename_with_dir)

    # with open(md_filename, 'w', encoding='utf8') as f:
    #     f.write(book_info_md_str)


def keyword_encode(s):
    """ 인코드를 이상하게 함: '파이썬' --> &#54028;&#51060;&#50028;
    # keyword_encode 로직은 교보문고 페이지의 javascript
    # 로직을 그대로 흉내내어 만들었음.
    """
    encoded = ''
    for ch in s:
        code = ord(ch)
        if code > 127:
            encoded += '&#' + str(code) + ';'
        else:
            encoded += str(code)
    return encoded


def search(keyword):
    data = {
        'vPstrKeyWord': keyword_encode(keyword),
        'vPstrCategory': 'TOT',
        'vPplace': 'top',
        'searchKeyword': quote(keyword.encode('euckr')),
    }

    search_url = "http://www.kyobobook.co.kr/search/SearchCommonMain.jsp"

    response = requests.post(search_url, data=data)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    book_info_md = []

    book_info_md.append('## BOOK SEARCH Info!')
    book_info_md.append(f"- 교보문고 서적검색: keyword = **'{keyword}'**")


    for tag in html_soup.select('.title a'):
        detail_url = tag['href']

        if 'detailViewKor' in detail_url:

            detail_url = urljoin(search_url, detail_url)
            title = tag.select_one('strong').text.strip()

            # print(title)
            # print(detail_url)
            partial_bold_title = title.replace(keyword, f" **'{keyword}'** ")
            book_info_md.append(f'1. [{partial_bold_title}]({detail_url})')

    book_info_md.append('---\n<br><br>')
    return book_info_md



if __name__ == '__main__':
    main()



""" Keyword = '파이썬'
Do it! 점프 투 파이썬
http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9788997390915&orderClick=LAG&Kc=

케라스 창시자에게 배우는 딥러닝(Deep Learning with Python)
http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791160505979&orderClick=LAG&Kc=
... continue ...
"""
