from dataclasses import dataclass, field
from urllib.parse import urljoin

import requests


@dataclass
class SpotifyClient:
    token: str
    API_URL: str = field(init=False, default="https://api.spotify.com/v1/")

    def send(self, url: str):
        url = urljoin(self.API_URL, url)

        headers = {"Authorization": f"Bearer {self.token}"}
        return requests.get(url, headers=headers)

    def me(self):
        return self.send("me")
