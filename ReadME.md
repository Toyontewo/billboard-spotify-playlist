
# 🎧 Billboard to Spotify Playlist Generator

Automatically create a **Spotify playlist** of the Billboard Hot 100 songs for any past date!  
This Python project scrapes the Billboard Hot 100 chart for a given date, searches Spotify for each track, and adds them to a private playlist in your Spotify account.


## Features
- 📅 Select any date (YYYY-MM-DD) to “travel back in time”
- 📰 Scrape Billboard Hot 100 songs using `BeautifulSoup`
- 🎶 Search Spotify for each song using advanced queries
- 📝 Automatically create a private playlist in your Spotify account
- ⏩ Add all found songs to the playlist in bulk


## Tech Stack
- **Python 3.9+**
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – for scraping Billboard
- [Spotipy](https://spotipy.readthedocs.io/) – Spotify Web API client
- [Requests](https://docs.python-requests.org/) – for fetching the Billboard page


## Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/toyontewo/billboard-spotify-playlist.git
cd billboard-spotify-playlist
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Typical dependencies:

```
beautifulsoup4
requests
spotipy
```


## ⚡ Usage

Run the script:

```bash
python billboard.py
```

Then:

* Enter a date in the format `YYYY-MM-DD` (e.g. `1999-08-14`)
* A browser window will open asking you to log into Spotify. Approve access.
* The script will scrape Billboard, search each song on Spotify, and create a playlist automatically 🎶




## How It Works:

1. **Scraping Billboard**
   Uses `BeautifulSoup` to extract the song titles and artist names from Billboard Hot 100 for the given date.

2. **Spotify Authentication**
   Uses `SpotifyOAuth` to authenticate your account and get permissions to create a playlist.

3. **Searching Spotify**
   Uses queries like `track:{title} artist:{artist} year:{YYYY}` to find the correct songs.

4. **Playlist Creation**
   Creates a private playlist in your Spotify account and adds all found URIs in batches of 100.


##  Scopes & Permissions

The project uses the following scope:

* `playlist-modify-private` → needed to create and edit private playlists.

