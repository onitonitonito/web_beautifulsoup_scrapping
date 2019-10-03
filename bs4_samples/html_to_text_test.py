"""
# html를 MD로 변환하는 LIB
# import tomd
# ---------
# 간단한 HTML 에 대해서 Markdown 텍스트로 변환
# 그런데, 복잡한 것은 에러 남.
#
\n\n\n"""
print(__doc__)

import os
import sys
import tomd as td
import html2text as ht

from pprint import pprint


HOME_NAME = "web_beautifulsoup_scrapping"
DIRS = os.path.dirname(__file__).partition(HOME_NAME)
HOME_DIR = DIRS[0] + DIRS[1] + "\\"

sys.path.append(HOME_DIR)

# FILE_NAME = "01_fruit.html" # N.G
FILE_NAME = "html_to_text_sample.html"    # O.K

FILE_W_DIR = HOME_DIR + "\\_statics\\" + FILE_NAME

with open(FILE_W_DIR, 'r', encoding='utf-8') as f:
    html = f.read()


a = td.Tomd(html).markdown
print(a)
