"""
# Q! : Python selenium tab feature works fine in Firefox but not in Chrome
# Site: https://stackoverflow.com/questions/35946391/
# python-selenium-tab-feature-works-fine-in-firefox-but-not-in-chrome
"""
# -------------------------------------------------------------
# I am working on the below script to open multiple website in new tabs.
# This is working fine in Firefox as expected.
# But it is not working in Chrome. It opens a new tab as the second tab,
# but the second website link opens in the first tab itself. Later again a new
# tab is opened as the third tab, then the third link opens in the first tab
# itself. The commented part ( 5 th line ) is how I call the chromedriver.exe.


import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from assets._config_security import user_email, user_password

print(__doc__)

browser = webdriver.Chrome()

def get_tab_first(url_target):
    browser.get(url_target)

def get_tab_additional(url_target):
    browser.execute_script(f"window.open('{url_target}', '_blank');")

def send_certi_keys(user_email, user_password):
    element_email = browser.find_element_by_id('user')
    element_email.send_keys(user_email)

    element_PW = browser.find_element_by_id('password')
    element_PW.send_keys(user_password)
    element_PW.submit()

def send_ctrl_t():
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')

def run_01():
    """00.WORKING! ... O.K with SENDING KEYS"""
    url_target = 'https://trello.com/login'
    get_tab_first(url_target)
    # get_tab_additional(url_target)

    time.sleep(3)
    send_certi_keys(user_email, user_password)
    send_ctrl_t()

def run_02():
    """01.ERROR : FAILED AT SENDING KEYS"""
    url_target = 'https://todoist.com/Users/showLogin'
    # get_tab_first(url_target)
    get_tab_additional(url_target)

    time.sleep(3)
    send_certi_keys(user_email, user_password)
    send_ctrl_t()

def run_03():
    """02.ERROR : FAILED AT SENDING KEYS"""
    url_target = 'https://asana.com/#login'
    # get_tab_first(url_target)
    get_tab_additional(url_target)

    time.sleep(3)
    emailElem = browser.find_element_by_id('login-email-login-modal')
    emailElem.send_keys(user_email)

    passwordElem = browser.find_element_by_id('login-password-login-modal')
    passwordElem.send_keys(user_password)

def main():
    run_01()
    run_02()
    run_03()

if __name__ == '__main__':
    """
    selenium.common.exceptions.NoSuchElementException: Message:
    no such element: Unable to locate element:
    {"method":"css selector","selector":"[id="login-email-login-modal"]"}
    (Session info: chrome=77.0.3865.90)
    """
    # TODO: to solve the issue : focusing element repeatidly

    main()
