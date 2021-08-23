from typing import List

from app.spotify.auth import SpotifyAuthScope, SpotifyAuth
from app.spotify.playlists import get_playlist


def get_repeated_tracks(client_id: str, client_secret: str, playlist_id: str) -> List[str]:
    spotify_auth = SpotifyAuth(client_id, client_secret, auth_scope=SpotifyAuthScope.PLAYLIST_READ_PRIVATE)
    spotify_auth.authorize()
    playlist = get_playlist(playlist_id, spotify_auth)
    repeated_tracks = []
    tracks = []
    for track in playlist["tracks"]["items"]:
        track_name = track["track"]["name"].strip().upper()
        if track_name not in tracks:
            tracks.append(track_name)
        else:
            repeated_tracks.append(track_name)

    return repeated_tracks
