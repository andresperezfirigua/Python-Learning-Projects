import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

FORM_URL = 'https://forms.gle/HjsXQBQ9sARn99'


class FormHandler:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(FORM_URL)
        time.sleep(4)

    def fill_in_form(self, property_details):
        answer_one = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )

        answer_one.click()
        answer_one.send_keys(property_details['address'])

        time.sleep(1)

        answer_two = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )

        answer_two.click()
        answer_two.send_keys(property_details['price'])

        time.sleep(1)

        answer_three = self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
        )

        answer_three.click()
        answer_three.send_keys(property_details['link'])

        time.sleep(1)

        self.driver.find_element(
            By.XPATH,
            '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
        ).click()

        time.sleep(3)

        self.driver.find_element(
            By.XPATH,
            '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
        ).click()

        time.sleep(2)
