import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

username = 'Email'
password = 'Password'
phone = 'Phone'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3700036791'
           '&f_AL=true'
           '&geoId=100876405'
           '&keywords=customer%20care%20representative'
           '&location=Colombia&refresh=true')

driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()

driver.find_element(By.ID, 'username').send_keys(username)

driver.find_element(By.ID, 'password').send_keys(password)

time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

time.sleep(10)

driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div['
                              '1]/div/div[1]/div[1]/div[4]/div/div/div/button/span').click()

time.sleep(2)

driver.find_element(By.XPATH,
                    '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[5]/div/div/div[1]/div/input'
                    ).send_keys(phone)

time.sleep(2)

driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button').click()

driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span').click()

driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]').click()

time.sleep(5)
