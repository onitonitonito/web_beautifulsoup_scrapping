"""
# 여러 개의 윈도우 창을 동시에 띄우기
"""
# 최초의 창은 브라우저실행 = browser.get(goto_url)
# 추가 창은 스크립트 실행 = browser.execute_script(script_strings)

import time
from selenium import webdriver

from assets.config_stocks import code_stock, show_dict
from assets.config_stocks import names, codes
from assets.config_stocks import site_finances
from assets.config_stocks import pop_top_windown, pop_script_window

print(__doc__)


def main():
    global browser

    show_dict()
    charts_total, charts_number_str = get_charts_quantity()
    end_number = get_charts_selected(charts_total, charts_number_str)
    print(f"*** Show you {end_number} chats! ***")

    browser = webdriver.Chrome()

    pop_top_windown(browser, 1)
    pop_script_window(browser, end_number, end_by=True)

    # TODO: get_charts_quantity ... has to be modified - [when getting array]


def get_charts_quantity():
    """ """
    global codes
    charts_total = len(codes)
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
