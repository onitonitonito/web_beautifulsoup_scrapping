import re
import os
from bs4 import BeautifulSoup

DESTIN_DIR = os.path.join(os.path.dirname(__file__),'')
# FNAME = '_reg_ex_drill.html'
FNAME = 'kevin_scrap.html'

with open(DESTIN_DIR + FNAME, mode='r', encoding='utf-8') as f:
    html_str = f.read()


bs_obj = BeautifulSoup(html_str, 'html.parser')

title_arr = re.findall(r'', bs_obj, flags=0)
print(title_arr)
