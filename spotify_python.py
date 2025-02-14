import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load dataset
df = pd.read_csv("spotify_top_music.csv")  # Update with your actual file name

# Spotify API credentials
client_id = "your_client_id"
client_secret = "your_client_secret"

# Authenticate
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_album_cover(song, artist):
    """Fetch album cover URL from Spotify API"""
    query = f"track:{song} artist:{artist}"
    results = sp.search(q=query, type="track", limit=1)
    
    if results["tracks"]["items"]:
        return results["tracks"]["items"][0]["album"]["images"][0]["url"]
    return None

# Add album cover URLs
df["album_cover_url"] = df.apply(lambda row: get_album_cover(row["track_name"], row["artist_name"]), axis=1)

# Save updated dataset
df.to_csv("spotify-2023-imagewithURls.csv", index=False)
