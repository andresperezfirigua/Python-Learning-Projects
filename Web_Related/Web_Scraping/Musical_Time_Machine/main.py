from bs4 import BeautifulSoup
import datetime
import requests

songs = []

day = 1

months_dict = {
    # 'March': 3,
    # 'June': 6,
    # 'September': 9,
    'November': 11
}

year = int(input('Which year do you want to travel to? Type year in this format YYYY, eg: "2020":\n'))

# Getting the top 40 songs from a specified year according to the Top 100 in Billboard
for key, value in months_dict.items():
    date = datetime.date(year=year, month=value, day=day)
    response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select(selector='.pmc-paywall li > h3:first-child')
    # titles = soup.select(selector='.pmc-paywall li > h3:first-child, li > h3:first-child + span')

    for title in titles:
        songs.append(title.getText().strip())

# print(len(songs))
# print(songs)
