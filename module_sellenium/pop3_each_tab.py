from selenium import webdriver

browser = webdriver.Chrome()

# browser.get("https://www.naver.com")
browser.execute_script("window.open('http://www.naver.com','_blank');")
browser.execute_script("window.open('http://www.daum.net','_blank');")
browser.execute_script("window.open('http://www.google.com','_blank');")
