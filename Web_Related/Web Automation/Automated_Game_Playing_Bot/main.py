import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, 'cookie')

start = time.time()
end = time.time()
print(time.ctime(start))
print(time.ctime(start + 5))
while end < start + 300:
    pause = end + 5
    if end < pause:
        cookie.click()
    else:
        # Check upgrade availability
        pass
    end = time.time()

time.sleep(10)
