### utils.py
def format_artist_list(sp, artist_ids):
    return [sp.artist(a)['name'] for a in artist_ids]