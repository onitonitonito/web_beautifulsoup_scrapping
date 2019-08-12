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

url_keys = {
        'naver' : ('http://search.naver.com', 'query'),
        'google' : ('http://www.google.com', 'q'),
        'daum' : ('http://www.daum.net', 'q'),
    }

# find_word = "ChromeDriver"
# URL=url_keys['naver'][0]
# KEY=url_keys['naver'][1]


def search_word(url_keys, site_name, find_word):
    _url = url_keys[site_name][0]
    _key = url_keys[site_name][1]

    browser = webdriver.Chrome()
    browser.get(_url)

    # script = f"window.open('{_url}','_blank');"
    # browser.execute_script(script)

    search_box = browser.find_element_by_name(_key)
    search_box.send_keys(find_word)
    # time.sleep(1)

    search_box.submit()
    # time.sleep(3)


search_word(url_keys, 'naver', '크롬드라이브')
search_word(url_keys, 'google', '크롬드라이브')
search_word(url_keys, 'daum', '크롬드라이브')
