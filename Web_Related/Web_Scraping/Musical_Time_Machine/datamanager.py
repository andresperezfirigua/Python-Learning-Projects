import requests
from bs4 import BeautifulSoup

URL = 'https://www.billboard.com/charts/hot-100'
SONG_TITLE = '.pmc-paywall li > h3:first-child'
SONG_ARTIST = '.pmc-paywall li > h3:first-child + span'


class DataManager:
    def __init__(self, date):
        self.songs = []
        self.request_url = f'{URL}/{date}'

    def get_website_content(self):
        return requests.get(self.request_url).text

    def scrape_songs(self):
        content = self.get_website_content()
        soup = BeautifulSoup(content, 'html.parser')
        titles = soup.select(selector=SONG_TITLE)
        artists = soup.select(selector=SONG_ARTIST)

        for item in range(len(titles) - 1):
            self.songs.append({'name': titles[item].getText().strip(), 'artist': artists[item].getText().strip()})

        print(f'{len(self.songs)} songs were scraped from Billboard website. {self.request_url}')
