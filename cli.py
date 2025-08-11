from argparse import ArgumentParser
from sys import platform
import music

apm = platform == "darwin"

parser = ArgumentParser(
    prog="dsi-music",
    description="Export songs from Spotify, Apple Music, or YouTube Music to your DSi automatically.",
    epilog="[Thank you. -Deltaion Lee]",
)

if apm:
    parser.add_argument(
        "-a",
        "--apple",
        action="store_true",
        help="download from the currently playing playlist",
    )
parser.add_argument(
    "-s", "--spotify", help="provide a playlist link", dest="spotify-link"
)
parser.add_argument(
    "-y", "--youtube", help="provide a playlist or song link", dest="youtube-link"
)
parser.add_argument(
    "-n",
    "--indirect",
    help="indirectly match tracks (for youtube playlists)",
    action="store_true",
)

args = parser.parse_args()

if apm:
    apple = args.apple
spotify = args.__dict__["spotify-link"]
youtube = args.__dict__["youtube-link"]
indirect = args.indirect

if indirect and youtube is None:
    raise NotImplementedError(
        "indirect matching is only an option for youtube playlists"
    )

log_response = '%s playlist "%s" indexed. Backing playlist via YouTube Music...'
if apm and apple:
    from music.apm import apm

    playlist = apm.playlist()
    response = input(
        'Would you like to download Apple playlist "%s"?\n(Y/N) > ' % playlist.name
    ).lower()
    if response.startswith("n"):
        quit()
    print(log_response % ("Apple", playlist.name))
    music.ytm.playlist(playlist)
if spotify is not None:
    from music.sfy import sfy

    playlist = sfy.playlist(spotify)
    print(log_response % ("Spotify", playlist.name))
    music.ytm.playlist(playlist)
if youtube is not None:
    print("Downloading YouTube song/playlist...")
    music.ytm.download(youtube)
