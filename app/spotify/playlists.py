import json

import requests

from app.spotify import urls
from app.spotify.auth import SpotifyAuth


class GetPlaylistException(Exception):
    pass


def get_playlist(playlist_id: str, auth: SpotifyAuth) -> dict:
    final_url = urls.PLAYLIST_BY_ID.format(playlist_id)
    headers = {"Authorization": "Bearer {}".format(auth.get_access_token())}
    response = requests.get(url=final_url, headers=headers)
    if response.status_code != 200:
        print("failed to get playlist by id")
        print("response body: {}".format(response.content))
        print("status code: {}".format(response.status_code))
        raise GetPlaylistException("failed to get playlist by id")

    return json.loads(response.content)
