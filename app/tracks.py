from difflib import SequenceMatcher
from typing import List

from app.spotify.auth import SpotifyAuthScope, SpotifyAuth
from app.spotify.playlists import get_playlist


def get_similar_tracks(client_id: str, client_secret: str, playlist_id: str, similarity_threshold: float = 85):
    similar_tracks = []
    all_tracks = __get_tracks(client_id, client_secret, playlist_id)
    for track in all_tracks:
        similarities = __get_similarities(track, all_tracks, similarity_threshold)
        similar_tracks.append({"name": track["name"], "similarities": similarities})

    return similar_tracks


def __get_tracks(client_id: str, client_secret: str, playlist_id: str) -> List[dict]:
    spotify_auth = SpotifyAuth(client_id, client_secret, auth_scope=SpotifyAuthScope.PLAYLIST_READ_PRIVATE)
    spotify_auth.authorize()
    playlist = get_playlist(playlist_id, spotify_auth)
    return list(map(lambda x:
                    {"id": x["track"]["id"], "name": x["track"]["name"].upper()}, playlist["tracks"]["items"]))


def __get_similarities(track: dict, tracks_list: List[dict], threshold: float) -> List[dict]:
    similar_tracks = []
    for current_track in tracks_list:
        if current_track["id"] != track["id"]:
            similarity = __track_similarity(track["name"], current_track["name"])
            if similarity >= threshold:
                similar_tracks.append({
                    "track": current_track["name"],
                    "similarity": similarity
                })

    return similar_tracks


def __track_similarity(track: str, other_track: str) -> float:
    similarity = SequenceMatcher(None, track, other_track).ratio() * 100
    return round(similarity, 2)
