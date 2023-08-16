from bs4 import BeautifulSoup
import requests

website = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
website_source = website.text

soup = BeautifulSoup(website_source, 'html.parser')

movies = soup.findAll(name='h3', class_='listicleItem_listicle-item__title__hW_Kn')

movies.reverse()

movie_titles = [movie.getText() for movie in movies]

with open(file='best_movies.txt', mode='w') as file:
    for movie in movie_titles:
        file.write(f'{movie}\n')
