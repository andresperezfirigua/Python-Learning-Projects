import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, 'cookie')

current_time = time.time()
game_duration = current_time + 60
end = time.time()
next_pause = end + 5

while end < game_duration:
    if end < next_pause:
        cookie.click()
    else:
        upgrades = driver.find_elements(By.XPATH, '/html/body/div[4]/div[5]/div/div')

        available_upgrades = [upgrade for upgrade in upgrades if upgrade.get_attribute('class') != 'grayed']

        available_upgrade = int(available_upgrades[-1].find_element(By.XPATH, './/b').get_attribute('textContent').split(' ')[-1])

        accumulated_cookies = int(driver.find_element(By.ID, 'money').get_attribute('textContent'))

        if accumulated_cookies > available_upgrade:
            available_upgrades[-1].click()

        next_pause = end + 5

    end = time.time()

print(driver.find_element(By.ID, 'cps').get_attribute('textContent'))
time.sleep(10)
