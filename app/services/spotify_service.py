import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def get_spotify_client():
    """Authenticate and return a Spotify client instance."""
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise EnvironmentError("Spotify credentials are not set in environment variables.")

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

def get_songs_by_emotion(emotion):
    """Fetch a list of songs based on the detected emotion."""
    # Map emotions to genres
    emotion_to_genre = {
        "joy": "happy",
        "sorrow": "sad",
        "anger": "angry",
        "surprise": "upbeat"
    }

    genre = emotion_to_genre.get(emotion.lower(), "chill")
    spotify_client = get_spotify_client()

    # Search for tracks based on genre
    results = spotify_client.search(q=f"genre:{genre}", type="track", limit=5)
    songs = []
    for track in results['tracks']['items']:
        songs.append(f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")

    return songs
