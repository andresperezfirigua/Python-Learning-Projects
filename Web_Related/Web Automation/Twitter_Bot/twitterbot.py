import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

TWITTER_USERNAME = 'Username'
TWITTER_PASSWORD = 'Password'


class TwitterBot:
    def __init__(self):
        self.up = None
        self.down = None
        chrome_options = Options()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
        ).click()
        time.sleep(100)
        self.down = float(
            self.driver.find_element(
                By.XPATH,
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                '1]/div[1]/div/div[2]/span'
            ).get_attribute('textContent')
        )
        self.up = float(
            self.driver.find_element(
                By.XPATH,
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                '1]/div[2]/div/div[2]/span'
            ).get_attribute('textContent')
        )

    def tweet_at_provider(self, promised_down, promised_up):
        self.driver.get('https://twitter.com/')
        self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div'
        ).click()

        time.sleep(2)

        username = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
            '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
            '2]/div/input'
        )

        username.send_keys(TWITTER_USERNAME)

        self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div['
            '6]/div/span/span'
        ).click()

        time.sleep(5)

        try:
            password = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                '3]/div/label/div/div[2]/div[1]/input'
            )

            password.send_keys(TWITTER_PASSWORD)

            self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div['
                '1]/div/div/div/div/span/span'
            ).click()

            time.sleep(7)

        except NoSuchElementException:
            time.sleep(3)
            username_confirmation = self.driver.find_element(
                By.XPATH,
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div['
                '2]/label/div/div[2]/div/input'
            )

            username_confirmation.send_keys(TWITTER_USERNAME)

            self.driver.find_element(
                By.XPATH,
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div'
            ).click()

            time.sleep(3)

            password = self.driver.find_element(
                By.XPATH,
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div['
                '3]/div/label/div/div[2]/div[1]/input'
            )

            password.send_keys(TWITTER_PASSWORD)

            self.driver.find_element(
                By.XPATH,
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div['
                '1]/div/div/div/div/span/span'
            ).click()

            time.sleep(7)

        tweet = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div'
        )

        tweet.send_keys(f'Hey Internet Provider, why is my internet speed {self.down} down/ {self.up} up '
                        f'when I pay for {promised_down} down/{promised_up} up?')

        self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div['
            '2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span'
        ).click()
