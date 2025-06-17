### auth.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_spotify_client(client_id, client_secret, redirect_uri, scope):
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope,
        show_dialog=True,
        cache_path=".spotifycache"
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    user_id = sp.current_user()['id']
    return sp, user_id