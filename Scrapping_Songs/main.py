import os

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
print(CLIENT_ID)
print(CLIENT_SECRET)

date = input(
    "Which year do you want to travel to? Type the date in this formet: YYYY-MM-DD: "
)
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=url)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

songs = [
    titleElement.string.strip()
    for titleElement in soup.select(".o-chart-results-list-row .c-title")
]
print(songs)

# Connecting with Spotify


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope="playlist-modify-private",
        redirect_uri="https://www.exampleurl.org",
        show_dialog=True,
        cache_path="token.txt",
    ),
)
# sp.user_playlist_create()
print(sp.current_user())
