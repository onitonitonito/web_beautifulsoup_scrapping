"""
# config_stocks.py - variables
"""
# apply: multi_pop_tabs / stock_weekly_chart.ipynb

print(__doc__)

import os
import random

name_home = "module_sellenium"

get_dir_by = (lambda x: "".join(os.path.dirname(__file__).partition(x)[:2])+"\\")
dir_home = get_dir_by(name_home)
dir_works = dir_home + "works\\"

# 조화할수 있는 targets를 정의한다. 총 7가지
targets = ['day','week','month3','year','year3','year5','year10']

code_stock = {
    '제닉': '123330',
    '휴메딕스': '200670',
    '대원미디어': '048910',
    '마크로젠': '038290',

    '아모레G': '002790',
    '내츄럴엔도텍': '168330',
    '삼성전자': '005930',
    '카카오': '035720',

    '한진칼' : '180640',
    '대한항공' : '003490',

    '로보스타' : '090360',
    '파트론' : '091700',

    '셀트리온' : '068270',
    '아시아나항공' : '020560',

    'LG디스플레이': '034220',
    'LG이노텍' : '011070',

    '포스코케미칼': '003670',
    '삼성전기' : '009150',

    'NHN한국사이버결제' : '060250',
    'KG이니시스' : '035600',

    '네이버': '035420',
    'NCSOFT': '036570',
    '안랩': '053800',
}

# 딕셔너리내용을 names 와 codes 어레이로 바꾼다 ... index 일체화
names = [name for name in code_stock.keys()]
codes = [code for code in code_stock.values()]

# for selenium chromedriver
site_finances = 'https://finance.naver.com/item/main.nhn?code='

# for chart image ... URL/target/codes[i].png?sidcode=randomint_13
URL = "https://ssl.pstatic.net/imgfinance/chart/item/area/"

def show_dict():
    """ 전체 딕셔너리 내용을 finance_URL 합성으로 보여준다 """
    global names, codes, site_finances
    print("------"*5)
    for i, code in enumerate(codes):
        url_target = site_finances + code
        print(f" {i+1:02}.{names[i]:14} {url_target}")
    print("------"*5, "\n")

def show_names_codes(names, codes):
    """ HELPER() for main() : 관심arr에 (코드)+URL를 보여줌 """
    print(f"\nTargets = {targets}", flush=True)
    print("========"*5, flush=True)
    for i, name in enumerate(names):
        url_target = f"{site_finances}{codes[i]}&sidecode={get_sidecode(13)}"
        print(f"{i+1:02}. {name} ({codes[i]})", flush=True)
        print(f" = {url_target}", flush=True)
    print("========"*5, flush=True)
    print("* 변경:'config_stocks.py' 의 변수를 수정.\n\n", flush=True)

def get_sidecode(n_digits=13, mode=0):
    """ 랜덤 숫자를 반환한다
    # get random n-digits(default=13) int.
    # using for cookie, css buster
    # mode=0 ... return exact 13-digits int > 12-digits
    # mode=1 ... return within 13-digits int = 1~13 digits
    """
    # return random.randint(1, 10**n_digits) ... NOT! What I want
    if mode:
        n_array = [f"{random.randint(0, 9)}" for n in range(n_digits)]
        random.shuffle(n_array)
        end = random.randint(2, n_digits+1)
        return int("".join(n_array[:end]))
    else:
        while 1:
            pick_random = random.randint(1, 10**n_digits)
            if len(f"{pick_random}") == n_digits:
                return pick_random

def get_names_codes_partial(index_partial):
    """파샬 리스트 작성한다
    # index_partial 입력받아, names/codes_partial 을 반환
    """
    names_partial, codes_partial = [], []
    for idx in index_partial:
        names_partial.append(names[idx])
        codes_partial.append(codes[idx])
    return names_partial, codes_partial

def pop_top_windown(browser, number):
    """첫번째 탭 : browser.get() """
    # top page = browser.get()
    global codes, site_finances
    url_top = site_finances + codes[number-1]
    browser.get(url_top)

    print()
    print(f" 01.{names[0]}({codes[0]})")

def pop_script_window(browser, numbers, end_by=True):
    """추가 되는 탭 : javascript - window.open"""
    # otehr tabs = browser.excute_script(javascript)
    global codes, names, site_finances
    if end_by:
        # 시작~ 끝번호, 끝번호를 선택하는 경우, end_by=True
        for i, code in enumerate(codes[1:numbers], 1):
            url_target = site_finances + code

            browser.execute_script(f"window.open('{url_target}', '_blank');")
            print(f" {i+1:02}.{names[i]}({code})")
    else:
        # 원하는 숫자Array를 입력하는 경우, [1,4,5,9,10] ... end_by=False
        for i, number in enumerate(numbers, 1):
            url_target = site_finances + codes[number-1]

            browser.execute_script(f"window.open('{url_target}', '_blank');")
            print(f" {number:02}.{names[number-1]}({codes[number-1]})")



if __name__ == '__main__':
    (names_partial, codes_partial) = get_names_codes_partial([1,2,3])
    show_names_codes(names_partial, codes_partial)
    pass
