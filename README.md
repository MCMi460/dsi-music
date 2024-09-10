# DSi Music
*Export songs from Spotify, Apple Music, or YouTube Music to your DSi automatically.*

## Running the app
[Install Python](https://www.python.org/downloads/) and download the required modules by running the following command in the repository's directory:  
`python -m pip install -r requirements.txt`  
Replace `python` with your valid command (i.e. `py` or `python3`). Then, run the app like so:  
`python app.py`

### Spotify
Spotify requires a [developer app](https://developer.spotify.com/) in order to proceed. Create one and a `secrets.py` inside of the [`music/`](/music) folder, and input the client id and client secret like the below:

```python
client_id = '[your client id]'
client_secret = '[your client secret]'
```

### Apple Music
Apple Music requires a Mac. Open the Music app and start playing a song in your targeted playlist to export to the DSi. Then, run the app.

### YouTube Music
YouTube Music offers an "indirect" track matching service. If enabled, the app will attempt to find the official music source uploaded to YouTube Music from keywords found in the linked video/playlist. It is not perfect, however, and like all other options, it may download incorrect tracks.
