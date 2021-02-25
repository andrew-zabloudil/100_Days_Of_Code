import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="./Day 46 Spotify Musical Time Machine/token.txt"
    )
)
user_id = sp.current_user()["id"]


date = input("What day do you want to travel to? Use the format YYYY-MM-DD:\n")
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url=url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
charts = soup.find_all("span", class_="chart-element__information")

songs = [
    (
        song.find("span", class_="chart-element__information__song").text,
        song.find("span", class_="chart-element__information__artist").text
    ) for song in charts
]

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Hot 100",
    public=False,
    collaborative=False,
    description=f"The Hot 100 songs from {date}."
)

items = []
for song in songs:
    result = sp.search(q=f"track:{song[0]} artist:{song[1]}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        items.append(uri)
    except IndexError:
        print(f"{song} cannot be found on Spotify. Skipped.")


sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=items
)

print("Finished.")
