import requests
import datetime
from bs4 import BeautifulSoup

URL = 'https://www.billboard.com/charts/hot-100'
HTML_ELEMENT = '.pmc-paywall li > h3:first-child'


class DataManager:
    def __init__(self, date):
        self.songs = []
        self.request_url = f'{URL}/{date}'

    def get_website_content(self):
        return requests.get(self.request_url).text

    def scrape_songs(self):
        content = self.get_website_content()
        soup = BeautifulSoup(content, 'html.parser')
        elements = soup.select(selector=HTML_ELEMENT)
        # elements = soup.select(selector='.pmc-paywall li > h3:first-child, li > h3:first-child + span')

        for element in elements:
            self.songs.append(element.getText().strip())
