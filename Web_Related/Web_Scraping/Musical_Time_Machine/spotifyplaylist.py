import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_SECRET = os.environ.get('SPOTIFY_SECRET')


def authenticate_with_spotify():
    scope = 'playlist-modify-private'  # "user-library-read"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_SECRET,
            redirect_uri="http://example.com",
            scope=scope
        )
    )

    return sp


class SpotifyPlaylist:
    def __init__(self):
        self.spotify = authenticate_with_spotify()

    def create_playlist(self, songs, date):
        track_uri_list = []
        username = self.spotify.current_user()['id']
        playlist = self.spotify.user_playlist_create(
            user=username,
            name=f'{date.year} Billboard 100',
            public=False,
            collaborative=False,
            description=f'This playlist is made of the top 100 songs from year {date.year}'
        )

        for song in songs:
            track = self.spotify.search(
                q=f'track:{song["name"]} year:{date.year}',
                type='track',
                limit=1
            )

            try:
                track_uri = track['tracks']['items'][0]['uri']
            except IndexError:
                print(f'"{song["name"]}" by {song["artist"]} was not found in Spotify.')
            else:
                track_uri_list.append(track_uri)

        self.spotify.playlist_add_items(playlist_id=playlist['id'], items=track_uri_list)

        print(f'{len(track_uri_list)} songs added to playlist')
