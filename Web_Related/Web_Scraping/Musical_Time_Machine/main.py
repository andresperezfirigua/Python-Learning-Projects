import datetime
from datamanager import DataManager
from spotifyplaylist import SpotifyPlaylist

year = int(input('Which year do you want to travel to? Type year in this format YYYY, eg: "2020":\n'))

date = datetime.date(year=year, month=11, day=1)

datamanager = DataManager(date)

datamanager.scrape_songs()

songs = datamanager.songs

spotify_playlist = SpotifyPlaylist()
spotify_playlist.create_playlist(songs, date)
