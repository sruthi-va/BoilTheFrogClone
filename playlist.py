### playlist.py
def get_top_track(sp, artist_id):
    try:
        tracks = sp.artist_top_tracks(artist_id)
        return tracks['tracks'][0]['uri'] if tracks['tracks'] else None
    except Exception as e:
        print(f"Error fetching top track for {artist_id}: {e}")
        return None

def create_playlist(sp, user_id, name, track_uris):
    playlist = sp.user_playlist_create(user=user_id, name=name)
    sp.playlist_add_items(playlist['id'], track_uris)