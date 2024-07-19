from ytmusicapi import YTMusic
from .models import Track, Playlist
from yt_dlp import YoutubeDL
from os.path import exists
from os import makedirs

yt = YTMusic()

opts = {
    'format': 'bestaudio[ext=m4a]/best',
    'postprocessors': [
        {
            'key': 'FFmpegMetadata',
            'add_metadata': True
        }
    ]
}

class ytm:
    def track(track:Track, *, folder:str = 'export') -> str:
        search_results = yt.search(
            ' '.join([track.name, track.artist, track.album]),
            filter = 'songs',
            limit = 1
        )
        id = search_results[0]['videoId']

        if not exists(folder):
            makedirs(folder)
        opts['outtmpl'] = f'{folder}/%(title)s.%(ext)s'

        with YoutubeDL(opts) as ydl:
            ydl.download(id)

        return id

    def playlist(playlist:Playlist):
        for track in playlist.tracks:
            ytm.track(track, folder = f'export/{playlist.name}')
