import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# chrome_driver_path = '../../../../chrome-win64/chrome.exe'
# chrome_options = Options()
# chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome()

# |------------------------------- Getting data from a website ---------------------------------------------|

# driver.get('https://www.amazon.com/-/es/Kasa-inteligente-interiores-movimiento-almacenamiento/dp/B08GHX9G5L/ref'
#            '=sr_1_5?qid=1692556677&s=electronics&sr=1-5&th=1')

# title = driver.find_element(By.ID, 'productTitle')
# print(title.text)

# prices = driver.find_elements(By.CLASS_NAME, 'a-offscreen')
# print(prices[0].get_attribute('textContent'))

# review_average = driver.find_elements(by=By.CSS_SELECTOR, value='#averageCustomerReviews i span')
# print(review_average[0].get_attribute('textContent'))

# estimated_eta = driver.find_element(
#     by=By.XPATH,
#     value='//*[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]/span/span[1]'
# )
# print(estimated_eta.get_attribute(name='textContent'))


# driver.get('https://www.python.org/')
#
# events_dict = {}
# event_index = 0
#
# events = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
#
# for event in events:
#     date = event.find_element(by=By.XPATH, value='.//time').get_attribute('datetime').split('T')[0]
#     name = event.find_element(by=By.XPATH, value='.//a').get_attribute('textContent')
#
#     events_dict[event_index] = {'date': date, 'name': name}
#
#     event_index += 1
#
# print(events_dict)


# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# article_count = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(article_count.text)


# |------------------------------- Interacting with a website ---------------------------------------------|

# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# article_count = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')

# article_count.click()
# time.sleep(5)

# edit_docs = driver.find_element(by=By.LINK_TEXT, value='anyone can edit')
# edit_docs.click()
# time.sleep(5)

# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)
# time.sleep(5)

# driver.get('http://secure-retreat-92358.herokuapp.com/')
# name = driver.find_element(By.NAME, 'fName')
# name.send_keys('Juan')
#
# lastname = driver.find_element(By.NAME, 'lName')
# lastname.send_keys('Ruiz')
#
# email = driver.find_element(By.NAME, 'email')
# email.send_keys('juan@myemail.com')
#
# time.sleep(3)
#
# submit = driver.find_element(By.XPATH, '/html/body/form/button')
# submit.click()
#
# time.sleep(3)
