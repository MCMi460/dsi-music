from .models import Track, Playlist
from sys import platform
from subprocess import run
assert platform == 'darwin'

class apm:
    def _run(script:str):
        return run(
            [
                'osascript',
                '-e',
                script
            ],
            capture_output = True
        ).stdout.decode('utf-8').strip()

    def playlist():
        playlist = Playlist(
            name = apm._run("""
                tell application "Music"
                    set exported to container of item 1 of selection
                    return name of exported
                end tell
            """)
        )

        tracks = apm._run("""
            set text item delimiters to "⎋"
            set exportedNames to {}
            tell application "Music"
                set exported to container of item 1 of selection
                set exports to tracks of exported
                repeat with exportSong in exports
                    set end of exportedNames to {name, artist, album} of exportSong
                end repeat
            end tell
            return exportedNames as text
        """).split('⎋')

        for i in range(0, len(tracks), 3):
            playlist.tracks.append(Track(
                name = tracks[i],
                artist = tracks[i+1],
                album = tracks[i+2]
            ))

        return playlist
