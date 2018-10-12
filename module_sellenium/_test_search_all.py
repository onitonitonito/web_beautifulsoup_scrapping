"""
#
# Optional argument, if not specified, will search path.
# driver = webdriver.Chrome('/Anaconda3/chromedriver')
# Registered already in sys.path '/Anaconda3/chromedriver'
# ChromeDriver Ver 2.43
"""
print(__doc__)


import time
from selenium import webdriver

URL_KEYS = {
        'naver' : ('http://search.naver.com', 'query'),
        'google' : ('http://www.google.com', 'q'),
        'daum' : ('http://www.daum.net', 'q'),
    }

# FIND_WORD = "ChromeDriver"
# URL=URL_KEYS['naver'][0]
# KEY=URL_KEYS['naver'][1]

DRIVER = webdriver.Chrome()


def search_word(url_name, word):
    _url = URL_KEYS[url_name][0]
    _key = URL_KEYS[url_name][1]
    _find_word = word

    # DRIVER = webdriver.Chrome()
    DRIVER.get(_url)

    search_box = DRIVER.find_element_by_name(_key)
    search_box.send_keys(_find_word)
    search_box.submit()


search_word('naver', '크롬드라이브')
search_word('google', '크롬드라이브')
search_word('daum', '크롬드라이브')

# time.sleep(5)
