"""
# 여러 개의 윈도우 창을 동시에 띄우기
# --------
# 최초의 창은 브라우저실행 = browser.get(goto_url)
# 추가 창은 스크립트 실행 = browser.execute_script(script_strings)
"""
# print(__doc__)

import time
from selenium import webdriver

from assets.config_stocks import site_finances
from assets.config_stocks import code_stock
from assets.functions_class import get_pop_script

names = [name for name in code_stock.keys()]
codes = [code for code in code_stock.values()]

# exec path was already set - chromedriver.exe
browser = webdriver.Chrome()


def main():
    # top page = browser.get()
    url_top = site_finances + codes[0]
    browser.get(url_top)

    print()
    print(f"{names[0]} ... {url_top}")

    # otehr tabs = browser.excute_script(javascript)
    for i, code in enumerate(codes[1:], 1):
        url_target = site_finances + code
        browser.execute_script(get_pop_script(url_target))
        print(f"{names[i]} ... {url_target}")



if __name__ == '__main__':
    main()







"""
# multi pop-up windows = browser.get() + call_windows_by_code()

# this is not functional
time.sleep(1)
browser.execute_script("window.close();")

# this works properly
time.sleep(5)
browser.quit()
"""
