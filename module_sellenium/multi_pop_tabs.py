"""
# 여러 개의 윈도우 창을 동시에 띄우기
# --------
# 최초의 창은 브라우저실행 = browser.get(goto_url)
# 추가 창은 스크립트 실행 = browser.execute_script(script_strings)
#
"""
# browser.get("https://www.naver.com")
# goto_dict = {
# 'naver_sports': 'https://sports.news.naver.com/index.nhn',
# 'daum_sports': 'https://sports.media.daum.net/sports/soccer/',
# 'google_home': 'http://www.google.com',
# }

print(__doc__)

import time

from selenium import webdriver
from assets.config_stocks import *



code_names = list(code_stock.keys())


def get_finance_site(site_finances, code_stock, code_name):
    mixed_string = site_finances + code_stock[code_name]
    return mixed_string


def get_finance_script(site_finances, code_stock, code_name):
    mixed_string = f"window.open('{site_finances + code_stock[code_name]}','_blank');"
    return mixed_string


def call_windows_by_code(code_names):
    for code_name in code_names:
        browser.execute_script(
            get_finance_script(site_finances, code_stock, code_name)
        )
        time.sleep(0.01)


# exec path was already set - chromedriver.exe
browser = webdriver.Chrome()

# overwrite on the same browser
# pop the 1st page and add others on different windows
browser.get(get_finance_site(site_finances, code_stock, code_names[0]))

# pops from seconds to the end
call_windows_by_code(code_names[1:])


# this is not functional
time.sleep(1)
browser.execute_script("window.close();")

# this works properly
time.sleep(5)
# browser.quit()
