"""
# Q! : Python selenium tab feature works fine in Firefox but not in Chrome
# Site: https://stackoverflow.com/questions/35946391/
# python-selenium-tab-feature-works-fine-in-firefox-but-not-in-chrome
# -------------------------------------------------------------
#
# I am working on the below script to open multiple website in new tabs.
# This is working fine in Firefox as expected.
# But it is not working in Chrome. It opens a new tab as the second tab,
# but the second website link opens in the first tab itself. Later again a new
# tab is opened as the third tab, then the third link opens in the first tab
# itself. The commented part ( 5 th line ) is how I call the chromedriver.exe.
"""
print(__doc__)



import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#
browser = webdriver.Chrome()


browser.get('https://trello.com/login')
# browser.execute_script("window.open('https://trello.com/login','tab_01');")
# time.sleep(5)

emailElem = browser.find_element_by_id('user')
emailElem.send_keys('test123@gmail.com')

passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('test12345')

# passwordElem.submit()

body = browser.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')
time.sleep(3)



browser.get('https://todoist.com/Users/showLogin')
# browser.execute_script("window.open('https://todoist.com/Users/showLogin','_blank');")

emailElem = browser.find_element_by_id('email')
emailElem.send_keys('test123@gmail.com')

passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys('test12345')

# passwordElem.submit()
# time.sleep(3)



# FAILED AT THIS POINT -----------------------------------------

# browser.get('https://asana.com/#login')
browser.execute_script("window.open('https://asana.com/#login','_blank');")

emailElem = browser.find_element_by_id('login-email-login-modal')
emailElem.send_keys('test123@gmail.com')

passwordElem = browser.find_element_by_id('login-password-login-modal')
passwordElem.send_keys('test12345')

# passwordElem.submit()
# time.sleep(3)
