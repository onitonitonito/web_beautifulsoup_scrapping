"""
# 여러 개의 윈도우 창을 동시에 띄우기
"""
# 최초의 창은 브라우저실행 = browser.get(goto_url)
# 추가 창은 스크립트 실행 = browser.execute_script(script_strings)

import time
from selenium import webdriver

from assets.config_stocks import code_stock
from assets.config_stocks import site_finances

print(__doc__)

names = [name for name in code_stock.keys()]
codes = [code for code in code_stock.values()]


def main():
    global browser

    charts_total, charts_number_str = get_charts_quantity()
    charts_number = get_charts_selected(charts_total, charts_number_str)
    print(f"*** Show you {charts_number} chats! ***")

    browser = webdriver.Chrome()

    pop_top_windown()
    pop_script_window(charts_number)

def pop_top_windown():
    """첫번째 탭 : browser.get() """
    # top page = browser.get()
    url_top = site_finances + codes[0]
    browser.get(url_top)

    print()
    print(f" 01.{names[0]}({codes[0]})")

def pop_script_window(charts_number):
    """추가되는 탭 : javascript - window.open"""
    # otehr tabs = browser.excute_script(javascript)
    for i, code in enumerate(codes[1:charts_number], 1):
        url_target = site_finances + code
        browser.execute_script(f"window.open('{url_target}', '_blank');")
        print(f" {i:02}.{names[i]}({code})")

def get_charts_quantity():
    """ """
    print("------"*5)
    for i, code in enumerate(codes):
        url_target = site_finances + code
        print(f" {i+1:02}.{names[i]:14} {url_target}")
    print("------"*5, "\n")
    charts_total = len(names)
    charts_number_str = input(f"How many charts(2~max.{charts_total})? [Ent]=All : ")
    return charts_total, charts_number_str

def get_charts_selected(charts_total, charts_number_str):
    """ """
     # = get_charts_quantity():
    if not charts_number_str.isnumeric():   # if 'ENTER'
        return charts_total
    else:                                   # if numeric
        if charts_number_str is '0':
            return 2                        # min. = 2
        else:
            return int(charts_number_str)



if __name__ == '__main__':
    main()
