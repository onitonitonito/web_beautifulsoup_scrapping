"""
# multi_tabs_random_pick.py - selected by pick number array like [1,6,8,23]
"""
#

import assets.script_run

from selenium import webdriver
from assets.config_stocks import site_finances
from assets.config_stocks import names, codes, code_stock
from assets.config_stocks import show_dict, pop_top_windown, pop_script_window

print(__doc__)

browser = webdriver.Chrome()

def main():
    # 딕셔너리 내용을 보여준다.
    show_dict()

    # 첫번째 페이지는 무조건 top로 입력해야 한다.
    pop_top_windown(browser, number=1)

    # 1, 2~4 까지 끝번호 지정으로 출력하는 경우
    pop_script_window(browser, numbers=4, end_by=True)

    # 1, 2,3,4 로 개별번호 지정으로 출력하는 경우
    pop_script_window(browser, numbers=[6,7,8], end_by=False)

    # 2번째 부터 Random-pick 입력하는 경우 (첫번째 입력도 고려)
    pop_script_window(browser, numbers=[11, 9, 17], end_by=False)


if __name__ == '__main__':
    # 테스트 끝!
    main()
