"""
# 셀레니움 / 크롬 드라이버 브라우저 자동제어 테스트
# 구글을 열고, 'ChromeDriver'에 대해서 키워드 검색 해주고,
# 잠시 대기후, 종료 - 각 단계마다, 5초씩 sleep
# ---------------------------------------------------
# 구글의 키워드 검색은 쿼리(q=)명령어 다음 파라메터로 실행
# 네이버는, &query=... / 구글, 다음은, &q=...
#
# https://tariat.tistory.com/397?category=678799
"""
# Optional argument, if not specified, will search path.
# browser = webdriver.Chrome('/Anaconda3/chromedriver')
# Registered already in sys.path '/Anaconda3/chromedriver'
# ChromeDriver Ver 2.43

print(__doc__)


import time
from selenium import webdriver


browser = webdriver.Chrome()
url_target = 'http://search.naver.com'


def show_search_result(browser, url_target):
    """ Naver 검색창에서 ChromeDriver 검색결과를 얻는다
    # 검색결과를 얻을때 까지 잠시 기다리다(time.sleep) 닫는다.
    """
    browser.get(url_target)
    time.sleep(3)

    search_box = browser.find_element_by_name('query')
    search_box.send_keys('ChromeDriver')
    search_box.submit()

    time.sleep(5)
    # browser.quit()

def login_naver(user_id, user_pw):
    """
    # 실패! : 자동입력 방지문자가 뜬다.
    # NAVER - 안전을 위해 비밀번호와 자동입력 방지문자를 입력해주세요.
    """

    browser.get(url=url_target)

    login_button = browser.find_element_by_class_name(name='lg_local_btn')
    login_button.click()
    time.sleep(3)


    # ID를 입력한다.
    id = browser.find_element_by_id(id_='id')
    id.send_keys(user_id)
    time.sleep(3)


    # PWD 를 입력한다.
    id = browser.find_element_by_id(id_='pw')
    id.send_keys(user_pw)
    time.sleep(3)

    naver_submit=browser.find_element_by_class_name(name='btn_global')
    naver_submit.click()

def main():
    """ # 주의! : ID/PW는 테스트 후, push 하지 말고 꼭! 지울 것! """
    USER_ID = 'id_here_remember!'
    USER_PW = 'password_here_and_clear'

    show_search_result(browser, url_target)
    login_naver(USER_ID, USER_PW)
    pass


if __name__ == '__main__':
    main()
