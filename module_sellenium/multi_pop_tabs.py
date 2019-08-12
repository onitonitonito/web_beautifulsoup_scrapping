"""
# 여러 개의 윈도우 창을 동시에 띄우기
# --------
# 최초의 창은 브라우저실행 = browser.get(goto_url)
# 추가 창은 스크립트 실행 = browser.execute_script(script_strings)
#
\n\n"""
print(__doc__)


import time
from selenium import webdriver

# browser.get("https://www.naver.com")
# goto_dict = {
# 'naver_sports': 'https://sports.news.naver.com/index.nhn',
# 'daum_sports': 'https://sports.media.daum.net/sports/soccer/',
# 'google_home': 'http://www.google.com',
# }

site_finances = 'https://finance.naver.com/item/main.nhn?code='
code_finances = {
    '제닉': '123330',
    '아모레G': '002790',
    '마크로젠': '038290',
    '대원미디어': '048910',
    '내츄럴엔도텍': '168330',
}

code_names = list(code_finances.keys())

def get_finance_site(site_finances, code_finances, code_name):
    mixed_string = site_finances + code_finances[code_name]
    return mixed_string

def get_finance_script(site_finances, code_finances, code_name):
    mixed_string = f"window.open('{site_finances + code_finances[code_name]}','_blank');"
    return mixed_string

def call_windows_by_code(code_names):
    for code_name in code_names:
        browser.execute_script(
            get_finance_script(site_finances, code_finances, code_name)
        )
        time.sleep(0.01)

# exec path was already set - chromedriver.exe
browser = webdriver.Chrome()

# browser.get() pops in same window
browser.get('http://www.google.com')

# overwrite on the same browser
browser.get(get_finance_site(site_finances, code_finances, '제닉'))

# pops from seconds to the end
call_windows_by_code(code_names[1:])


# # not functional
# time.sleep(1)
# browser.execute_script("window.close();")

# time.sleep(5)
# browser.quit()
