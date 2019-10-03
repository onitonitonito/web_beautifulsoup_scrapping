"""
# book_machine_learning.py - LESSON.01 : Book KUJIRA :: Machine learning.
"""
import os, sys                                          # 1
root_name = "web_beautifulsoup_scrapping"               # 2
root = "".join(os.getcwd().partition(root_name)[:2])    # 3
sys.path.insert(0, root)                                # 4
print(__doc__)

import _assets.script_run
from _assets.configs import *
from _assets.class_functions import *

url_target = 'http://api.aoikujira.com/ip/ini'

def simple_text_scraping():
    # READOUT DATA
    response = get_response(url_target, getter=2)
    temps = response.text.split("\n")

    # [print(temp) for temp in temps]

    result_dict = {}
    for temp in temps:
        if temp.find("=") > 0:
            (title, info) = temp.split("=")
            result_dict[title] = info


    # SHOW DATA Decoded
    TEXT = response.decode('UTF-8')

    print('(1) DATA = ', response)  # byte type 'str'
    print('(2) TEXT = ', TEXT)      # decoded 'str' with 'CODEC=UTF-8'

    [print(f"{title:20} : {info}") for (title, info) in result_dict.items()]

"""
# book_machine_learning.py - Naver finance USD to KRW
"""
import time


def get_USD2KRW_in_naver():
    # To bring HTML
    url_target = "http://finance.naver.com/marketindex/"
    # RES = req.urlopen(URL)
    response = get_response(url_target, getter=1)
    reload_intervaly = 0
    reload_sec = 10

    while True:
        # div class='head_info' 안에서 span class='value'
        krw = response.select_one('div.head_info > span.value').string    # 1,133.80

        # div class='head_info' 안에서 span class='change'
        differ = response.select_one('div.head_info > span.change').string  # 1.20

        # div class='head_info' 안에서 span class='blind' = 상승/하강(한글)
        change = response.select_one('div.head_info > span.blind').string   # down

        flt_krw = float(krw.replace(',',''))
        flt_differ = float(differ)

        reload_intervaly += 1
        print(f'\tRELOAD     : {reload_intervaly} times ({reload_sec}sec.)')
        print(f'\tUSD/KRW    : {flt_krw:,.2f} 원/$')
        print(f'\tDifference : {flt_differ:.2f} {change}')    # 상승/하강
        print("------------"*3 + "\n\n")
        # b'\xc3\x87\xc3\x8f\xc2\xb6\xc3\xb4'

        if reload_intervaly >= 3:
            print("Done!")
            break

        sys.stdout.flush()
        time.sleep(reload_sec)


if __name__ == '__main__':
    # simple_text_scraping()
    get_USD2KRW_in_naver()
    pass
