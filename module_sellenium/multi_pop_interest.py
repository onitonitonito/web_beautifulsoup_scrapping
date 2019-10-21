"""
# daum 에서 실시간 관심기사 창 띄우기
"""
# 최초의 창은 브라우저실행 = browser.get(goto_url)
# 추가 pop창은 스크립트 실행 = browser.execute_script(script_strings)
print(__doc__)

from selenium import webdriver

from assets.config_daum import tags
from assets.functions_class import get_pop_script

browser = webdriver.Chrome()


def main():
    # 첫번째 장 오픈
    browser.get(tags[0])

    # 팝업 텝 오픈
    browser.execute_script(get_pop_script(tags[1]))
    browser.execute_script(get_pop_script(tags[2]))
    browser.execute_script(get_pop_script(tags[3]))




if __name__ == '__main__':
    main()
