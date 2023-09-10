import requests
from bs4 import BeautifulSoup

URL = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds' \
      '%22%3A%7B%22north%22%3A37.90435066929138%2C%22east%22%3A-122.22184268359375%2C%22south%22%3A37.646007551899324' \
      '%2C%22west%22%3A-122.64481631640625%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A' \
      '%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22' \
      '%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B' \
      '%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C' \
      '%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22' \
      '%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D'


class DataManager:
    def __init__(self):
        self.properties = []

    def search_data(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
            'Cache-Control': 'max-age=0',
            'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/115.0.0.0 Safari/537.36',
        }

        data = requests.get(url=URL, headers=headers).text

        soup = BeautifulSoup(data, 'html.parser')

        web_elements = soup.find_all(
            name='div',
            class_='StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0 bKpguY property-card-data'
        )

        for element in web_elements:
            self.properties.append(
                {
                    'address': element.find(name='address').text,
                    'price': element.find(class_='PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr').text,
                    'link': element.find(class_='StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW '
                                                 'property-card-link').get('href')
                }
            )

        return self.properties
