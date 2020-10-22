from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from urllib.parse import urlencode, urljoin

import requests

from .consts import SCOPE

if TYPE_CHECKING:
    from weekly.config import Config


@dataclass
class AuthorizationClient:
    config: "Config"
    API_URL: str = field(init=False, default="https://accounts.spotify.com/")

    @property
    def callback_url(self) -> str:
        # This would be better with `url_for`, but that would cause too much fuss in dev.
        return urljoin(self.config["ROOT"], "callback")

    def authorization_url(self):

        params_data = {
            "client_id": self.config["SPOTIFY_CLIENT_ID"],
            "response_type": "code",
            "redirect_uri": self.callback_url,
            "scope": " ".join(SCOPE),
        }
        url = urljoin(self.API_URL, "authorize")
        return "?".join([url, urlencode(params_data)])

    def get_access_token(self, code: str) -> str:
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.callback_url,
        }
        url = urljoin(self.API_URL, "api/token")
        response = requests.post(
            url,
            auth=(self.config["SPOTIFY_CLIENT_ID"], self.config["SPOTIFY_CLIENT_SECRET"]),
            data=data,
        )
        print(response.json())
        return response.json()["access_token"]
