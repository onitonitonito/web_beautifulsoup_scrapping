"""
# Keyword search in Donga-Ilbo :: Couldn't find : parser libraryError lxml
# --- (1) Can't performed with CMD - lxml parser libraryError, DLL errors etc.
# --- (2) Only run with Anaconda env = Ipython, Jupyter, Spyder etc..
#
#
# http://news.donga.com/search
# ?p=
# &query=
# &check_news=1
# &more=1
# &sorting=3
# &search_date=1
# &v1=
# &v2=
# &range=3'
"""
print(__doc__)

# import lxml # can't find a tree builder : lxml. Install parser?
# from lxml import etree    # ImportError: DLL load failed:


import os
import sys

import urllib.request

from bs4 import BeautifulSoup
from urllib import parse

# 현재 화일이 있는 working dir.
work_dir = os.getcwd()

# C:\...web_beautifulsoup_scrapping\static\result\
dir_static_result = os.path.join(work_dir, *['static', 'result', '',])

# print(dir_static_result); quit()


TARGET_URL_BEFORE_PAGE_NUM = "http://news.donga.com/search?p="
TARGET_URL_BEFORE_KEWORD = '&query='
TARGET_URL_REST = '&check_news=1&more=1&sorting=3&search_date=1&v1=&v2=&range=3'


KEY_WORD = '사드'
PAGE_NUM = 2
OUT_F_NAME = '_1_thadd_article.pdb'

DESTIN_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'static', '_temp', '')


def get_link_from_news_title(page_num, URL, output_file):
    for i in range(page_num):
        current_page_num = 1 + i * 15
        position = URL.index('=')       # 'int' = 1st position
        URL_with_page_num = URL[: position + 1] + str(current_page_num) \
            + URL[position + 1:]
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml',
                             from_encoding='utf-8')
        for title in soup.find_all('p', 'tit'):
            title_link = title.select('a')
            article_URL = title_link[0]['href']
            get_text(article_URL, output_file)


def get_text(URL, output_file):
    source_code_from_url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
    content_of_article = soup.select('div.article_txt')

    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        output_file.write(string_item)


def main(argv):
    """
    # if len(argv) != 4:
    #     return
    # KEY_WORD = argv[1]
    # PAGE_NUM = int(argv[2])
    # OUT_F_NAME = argv[3]"""

    meta_string_on_top = 'KEY WORD = %s / PAGE NUMBER = %s / FILE_NAME = %s' % (
        KEY_WORD, PAGE_NUM, OUT_F_NAME) + '\n' + '^+^+^' + '\n'

    # ...com/search?p= | &query= |
    target_URL = TARGET_URL_BEFORE_PAGE_NUM \
        + TARGET_URL_BEFORE_KEWORD \
        + parse.quote(KEY_WORD) \
        + TARGET_URL_REST

    # print(type(parse.quote(KEY_WORD)))
    # print('----',parse.quote(KEY_WORD))

    output_file = open(DESTIN_DIR + OUT_F_NAME, 'w', encoding='utf-8')

    output_file.write(meta_string_on_top)      # write meta_string @TOP
    get_link_from_news_title(PAGE_NUM, target_URL, output_file)
    output_file.close()


if __name__ == '__main__':
    # main(sys.argv)
    pass
