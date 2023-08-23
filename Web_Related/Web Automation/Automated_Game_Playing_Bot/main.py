from selenium import webdriver
import time
chrome_driver_path = '../../../../chrome-win64/chrome.exe'

driver = webdriver.Chrome()
driver.get('https://www.amazon.com')
