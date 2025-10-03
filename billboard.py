import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

b_url = "https://www.billboard.com/charts/hot-100"
date = input("Which year do you wanna travel to? Type the date in this format YYYY-MM-DD: \n")

URL = f"{b_url}/{date}"


response = requests.get(url=URL, headers=headers)
page = response.text
# print(page)

soup = BeautifulSoup(page, "html.parser")
titles = soup.find_all("li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-padding-l-050 lrv-u-padding-l-00@mobile-max u-max-width-397")
song_list = []
for t in titles:
    h3 = t.find("h3")
    song_title = h3.text.strip() if h3 else None

    a = t.find("a")
    if a:
        artist = a.text.strip()
    else:
        span = t.find("span", class_="c-label")
        artist = span.text.strip() if span else None
        print(artist)

    if song_title and artist:
        song_list.append({"title": song_title, "artist": artist})

# print(songs)

client_credentials_manager = SpotifyClientCredentials(
    client_id="bea112b912e645f78fa0bf4629cdccfa",
    client_secret="6215811657a040dfa5d92fdc8724e88f"
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q="Burna Boy", type="artist", limit=1)
# print(results)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="bea112b912e645f78fa0bf4629cdccfa",
    client_secret="6215811657a040dfa5d92fdc8724e88f",
    redirect_uri="https://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path=".cache",
    username="Toyo",
))

user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Hot 100 - {date}", public=False)

playlist_id = playlist["id"]

print("Playlist created:", playlist["external_urls"]["spotify"])
track_uris = []

for song in song_list:
    title = song["title"]
    artist = song["artist"]
    query = f"track:{title} artist:{artist} year:{date[:4]}"

    try:
        result = sp.search(q=query, type="track", limit=1)
        tracks = result["tracks"]["items"]

        if tracks:
            uri = tracks[0]["uri"]
            track_uris.append(uri)
            print(f"✅ Found: {title} - {artist}")
        else:
            print(f"❌ Not found: {title} - {artist}")

    except Exception as e:
        print(f"⚠️ Error searching for '{title}': {e}")

pprint(track_uris)
sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
