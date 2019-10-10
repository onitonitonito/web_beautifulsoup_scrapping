"""
# book_macnine_learning.py - simple scrapping examples
# - from M/L book by Kujira.
"""
# root path 를 sys.path.insert 시키기 위한 코드 ... 최소 4줄 필요------------
import os, sys                                                          # 1
root_name = "web_beautifulsoup_scrapping"                               # 2
root = "".join(os.getcwd().partition(root_name)[:2])                    # 3
sys.path.insert(0, root)                                                # 4
# -------------------------------------------------------------------------

import re
import _assets.script_run
from _assets.class_functions import (get_html_soup,
                                    get_finders,
                                    get_regex_extracts)

print(__doc__)

def main():
    keyword = "샤오미+체지방"
    price_cut_range = (10_000, 100_000)
    show_shopping_naver(keyword, *price_cut_range)

    show_api_response_scrapping()
    show_usd2krw_naver_finance()
    pass


def show_shopping_naver(keyword, low_cut, high_cut):
    """
    # made this for practice, quit not that effective
    # price range's limited by low~high cut value.
    """
    # TODO: this can be solved with query option

    # tags = ['div', {'class': 'co_relation_srh'}]    # 연관검색어
    tags = ['div', {'class': 'info'}]                 # 상품정보

    price_pattern = "\d+,\d+"
    date_pattern = "등록일[ ]\d{4}[.]\d{2}"


    url_target = "https://search.shopping.naver.com/search/all.nhn?query="
    url_combined = url_target + keyword

    html_soup = get_html_soup(url_combined, getter=1)
    finders = get_finders(tags, html_soup)

    index_find = 0

    print("----------"*5)
    print(f"keyword = {keyword}")
    print(f"price_range = {low_cut:,}원 ~ {high_cut:,}원")
    print("----------"*5)
    for find in finders:
        temp_strs = str(find.text).replace("\t", "")
        temp_strs = temp_strs.replace("  ", "")
        temp_strs = temp_strs.split("\n")

        made_strs = [str.strip()
                    for str in temp_strs
                    if str is not ""
                    ]

        if made_strs[0] != "해외":
            rule = keyword.split("+")[0]
            titles = made_strs[0].partition(rule)
            title = "".join(titles[2:])
            title = title[:30]
            _blank = " "*9

            price = re.compile(price_pattern).findall(str(find))
            date = re.compile(date_pattern).findall(str(find))
            if date:
                date = date[0].replace("등록일 ", "")

            if high_cut >= int(price[0].replace(",","")) >= low_cut:
                if date:
                    print(f"{index_find:02}.{price[0]:>7}원 ({date:7}){title:.<25}")
                else:
                    print(f"{index_find:02}.{price[0]:>7}원 {_blank}{title:.<25}")

                index_find += 1
    print("----------"*5)


def show_api_response_scrapping():
    """
    # book_machine_learning.py - Book by KUJIRA :: Machine learning.
    # using: class_functions.get_html_soup()
    """
    # READOUT DATA
    url_target = 'http://api.aoikujira.com/ip/ini'
    html_soup = get_html_soup(url_target, getter=2)
    rows = html_soup.text.split("\n")

    [print(row) for row in rows]          # for test!

    # store in result_dict
    result_dict = {}
    for row in rows:
        if row.find("=") > 0:
            (title, info) = row.split("=")
            result_dict[title] = info


    # show data decoded by 'utf8' ... html_soup = <class 'bs4.BeautifulSoup'>
    # html_soup_str = str(object=html_soup) # the same
    html_soup_str = html_soup.decode('UTF-8')

    print('(1) DATA = ', html_soup)      # byte type 'str'
    print('(2) TEXT = ', html_soup_str)  # decoded 'str' with 'CODEC=UTF-8'

    print("---- dictionary ----")
    [print(f"{title:20} : {info}") for (title, info) in result_dict.items()]


def show_usd2krw_naver_finance():
    """
    # book_machine_learning.py - LESSON.02 : Naver finance USD to KRW
    # using: class_functions.get_html_soup()
    """
    import time
    # To bring HTML
    reload_sec = 10
    reload_intervaly = 0
    url_target = "http://finance.naver.com/marketindex/"

    # RES = req.urlopen(URL)
    html_soup = get_html_soup(url_target, getter=1)

    while True:
        # div class='head_info' 안에서 span class='value'
        krw = html_soup.select_one('div.head_info > span.value').string    # 1,133.80

        # div class='head_info' 안에서 span class='change'
        differ = html_soup.select_one('div.head_info > span.change').string  # 1.20

        # div class='head_info' 안에서 span class='blind' = 상승/하강(한글)
        change = html_soup.select_one('div.head_info > span.blind').string   # down

        flt_krw = float(krw.replace(',',''))
        flt_differ = float(differ)

        reload_intervaly += 1
        print(f'\tUSD/KRW    : {flt_krw:,.2f} 원/$')
        print(f'\tDifference : {flt_differ:.2f} {change}')    # 상승/하강
        print(f'\tRELOAD     : {reload_intervaly} times ({reload_sec}sec.)')
        print("------------"*3 + "\n\n")
        # b'\xc3\x87\xc3\x8f\xc2\xb6\xc3\xb4'

        if reload_intervaly >= 3:
            print("Done!")
            break

        sys.stdout.flush()
        time.sleep(reload_sec)



if __name__ == '__main__':
    main()
