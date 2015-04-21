from selenium import webdriver

browser = webdriver.Chrome("c:\\chromedriver\\chromedriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title