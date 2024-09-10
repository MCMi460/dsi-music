from ytmusicapi import YTMusic
from .models import Track, Playlist
from yt_dlp import YoutubeDL
from os.path import exists
from os import makedirs
from re import findall

yt = YTMusic()

opts = {
    'format': 'bestaudio[ext=m4a]/best',
    'postprocessors': [
        {
            'key': 'FFmpegMetadata',
            'add_metadata': True
        },
        {
            'key': 'EmbedThumbnail'
        }
    ],
    'writethumbnail': True,
    'ignoreerrors': True
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
    
    def download(url:str, *, indirect:bool = False, folder:str = 'export'):
        playlist_id = findall(
            r'list=([^&#]*)',
            url
        )
        if len(playlist_id) > 0:
            title = yt.get_playlist(
                playlist_id[0],
                limit = 0
            )['title']
            folder += f'/{title}'
        
        if not exists(folder):
            makedirs(folder)
        opts['outtmpl'] = f'{folder}/%(title)s.%(ext)s'

        with YoutubeDL(opts) as ydl:
            item = ydl.extract_info(url, download = not indirect)
            if indirect:
                if item.get('_type') == 'playlist':
                    for song in item['entries']:
                        ytm.track(Track(
                            name = song['title'],
                            artist = song['uploader'],
                            #album = song['']
                        ), folder = folder)
                else:
                    ytm.track(Track(
                        name = item['title'],
                        artist = item['uploader']
                    ))
