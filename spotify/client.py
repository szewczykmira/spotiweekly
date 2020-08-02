from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List
from urllib.parse import urlencode, urljoin

from flask import url_for

from .consts import SCOPE, SPOTIFY_AUTHORIZATION_URL

if TYPE_CHECKING:
    from .config import Config


@dataclass
class SpotifyAuthenticationClient:
    config: "Config"

    @property
    def auth_url(self):
        callback_url = url_for("weekly.callback")
        params_data = {
            "client_id": self.config["SPOTIFY_CLIENT_ID"],
            "response_type": "code",
            "redirect_uri": urljoin(self.config["HOST"], callback_url),
            "scope": " ".join(SCOPE),
        }
        params = urlencode(params_data)
        return "?".join([SPOTIFY_AUTHORIZATION_URL, params])
