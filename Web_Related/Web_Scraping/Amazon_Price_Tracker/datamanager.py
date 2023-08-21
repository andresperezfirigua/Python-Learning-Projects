import requests
from bs4 import BeautifulSoup


class DataManager:
    def __init__(self):
        self.price = None
        self.product = ''
        self.url = 'https://www.amazon.com/-/es/Kasa-inteligente-interiores-movimiento-almacenamiento/dp/B08GHX9G5L/ref=sr_1_5?qid' \
      '=1692556677&s=electronics&sr=1-5&th=1'

    def get_website_content(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/115.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'
        }
        return requests.get(url=self.url, headers=headers).text

    def scrape_price(self):
        content = self.get_website_content()
        soup = BeautifulSoup(content, 'lxml')
        price_result = soup.select_one(selector='#corePrice_feature_div .a-offscreen')
        title_result = soup.find(name='span', id='productTitle')
        self.price = float(price_result.getText().split('$')[1])
        self.product = title_result.getText().strip()
