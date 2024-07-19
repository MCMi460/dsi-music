from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
try:
    from .secrets import client_id, client_secret
except (ModuleNotFoundError, ImportError):
    raise FileNotFoundError('spotify playlists require'
    + ' a valid client id and secret in secrets.py.'
    + ' See https://developer.spotify.com/')
from requests import get
from re import findall
from .models import Track, Playlist

sp = Spotify(
    auth_manager = SpotifyClientCredentials(
        client_id = client_id,
        client_secret = client_secret
    )
)

class sfy:
    # Deprecated
    def _user_id(url:str) -> str:
        return findall(
            r'\/user\/.+?(?=")', # how 2 regex ???
            get(url).text
        )[0][6:]

    def playlist(url:str) -> Playlist:
        playlist_id = url.split('/')[-1].split('?')[0]

        # Pull playlist page
        page = sp.playlist(playlist_id)

        # Create playlist object
        playlist = Playlist(
            name = page['name'],
            creator = page['owner']['display_name'],
        )

        # Pull all tracks into tracks variable
        page = page['tracks']
        tracks = page['items']
        while page['next']:
            page = sp.next(page)
            tracks.extend(page['items'])

        # Reformat tracks as typing.List[Track]
        for i, track in enumerate(tracks):
            track = track['track']
            tracks[i] = Track(
                name = track['name'],
                artist = track['artists'][0]['name'],
                album = track['album']['name']
            )

        # Add tracks to playlist object
        playlist.tracks = tracks

        return playlist
