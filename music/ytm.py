from ytmusicapi import YTMusic
from .models import Track, Playlist

yt = YTMusic()

class ytm:
    def track(track:Track):
        search_results = yt.search(
            ' '.join([track.name, track.artist, track.album]),
            filter = 'songs'
        )
        return search_results

    def playlist(playlist:Playlist):
        for track in playlist.tracks:
            print(ytm.track(track))
