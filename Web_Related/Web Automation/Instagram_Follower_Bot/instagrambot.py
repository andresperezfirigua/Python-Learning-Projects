import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

INSTAGRAM_USERNAME = 'Username'
INSTAGRAM_PASSWORD = 'Password'


class InstagramBot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        pass

    def find_followers(self, account):
        self.driver.get(f'https://www.instagram.com/{account}/followers/')

    def follow(self):
        pass
