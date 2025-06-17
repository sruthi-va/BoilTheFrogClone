### artist_graph.py
from collections import deque
import time

def get_related_artists(sp, artist_id, retries=3):
    for attempt in range(retries):
        try:
            related = sp.artist_related_artists(artist_id)
            return [artist['id'] for artist in related['artists']]
        except Exception as e:
            print(f"Attempt {attempt+1} failed fetching related artists for {artist_id}: {e}")
            time.sleep(1)
    print(f"Skipping artist {artist_id} after {retries} failed attempts.")
    return []


def get_artist_id(sp, artist_name):
    result = sp.search(q=artist_name, type='artist', limit=1)
    return result['artists']['items'][0]['id'] if result['artists']['items'] else None

def find_artist_path(sp, start_id, end_id, max_depth=6):
    queue = deque([[start_id]])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end_id:
            return path

        if current in visited or len(path) > max_depth:
            continue

        visited.add(current)
        for neighbor in get_related_artists(sp, current):
            if neighbor not in visited:
                queue.append(path + [neighbor])
    return None