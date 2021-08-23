import json
from datetime import datetime, timedelta
from enum import Enum

import requests

from app.spotify import urls


class SpotifyAuthScope(Enum):
    IMAGE_UPLOAD = "ugc-image-upload"
    PLAYLIST_MODIFY_PRIVATE = "playlist-modify-private"
    PLAYLIST_READ_PRIVATE = "playlist-read-private"
    PLAYLIST_MODIFY_PUBLIC = "playlist-modify-public"
    PLAYLIST_READ_COLLABORATIVE = "playlist-read-collaborative"
    USER_READ_PRIVATE = "user-read-private"
    USER_READ_EMAIL = "user-read-email"
    USER_READ_PLAYBACK_STATE = "user-read-playback-state"
    USER_MODIFY_PLAYBACK_STATE = "user-modify-playback-state"
    USER_READ_CURRENTLY_PLAYING = "user-read-currently-playing"
    USER_LIBRARY_MODIFY = "user-library-modify"
    USER_LIBRARY_READ = "user-library-read"
    USER_READ_PLAYBACK_POSITION = "user-read-playback-position"
    USER_READ_RECENTLY_PLAYED = "user-read-recently-played"
    USER_TOP_READ = "user-top-read"
    APP_REMOTE_CONTROL = "app-remote-control"
    STREAMING = "streaming"
    USER_FOLLOW_MODIFY = "user-follow-modify"
    USER_FOLLOW_READ = "user-follow-read"


class RetrieveAccessTokenException(Exception):
    pass


class SpotifyAuth:
    __headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    def __init__(self, client_id: str, client_secret: str, auth_scope: SpotifyAuthScope):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__auth_scope = auth_scope
        self.__authorization = None
        self.__authorization_date = None

    def authorize(self) -> dict:
        if self.__authorization is None or self.is_expired():
            return self.__new_authorization()
        else:
            return self.__authorization

    def is_expired(self) -> bool:
        now = datetime.now()
        expiring_datetime = self.__authorization_date + timedelta(seconds=self.__authorization["expires_in"])
        return now > expiring_datetime

    def get_current_authorization(self):
        return self.__authorization

    def get_access_token(self):
        return self.__authorization["access_token"]

    def __new_authorization(self) -> dict:
        data = {
            "grant_type": "client_credentials",
            "client_id": self.__client_id,
            "client_secret": self.__client_secret,
            "scope": self.__auth_scope.value
        }

        response = requests.post(url=urls.AUTH_URL, data=data, headers=self.__headers)

        if response.status_code != 200:
            print("retrieve access token failed. status code: {}".format(response.status_code))
            print("response body: {}".format(response.content))
            raise RetrieveAccessTokenException("failed to retrieve access token")

        self.__authorization_date = datetime.now()
        self.__authorization = json.loads(response.content)
        return self.__authorization
