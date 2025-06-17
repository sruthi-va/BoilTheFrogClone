### main.py
from auth import get_spotify_client
from artist_graph import get_artist_id, find_artist_path
from playlist import get_top_track, create_playlist
from utils import format_artist_list

if __name__ == '__main__':
    sp, user_id = get_spotify_client(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE)

    start_artist = "Coldplay"
    end_artist = "Imagine Dragons"



    start_id = get_artist_id(sp, start_artist)
    end_id = get_artist_id(sp, end_artist)

    path = find_artist_path(sp, start_id, end_id)

    if path:
        print(f"Found path: {format_artist_list(sp, path)}")
        track_uris = [get_top_track(sp, artist_id) for artist_id in path if get_top_track(sp, artist_id)]
        create_playlist(sp, user_id, f"{start_artist} to {end_artist} Journey", track_uris)
        print("Playlist created!")
    else:
        print("Could not find a path between the artists.")
