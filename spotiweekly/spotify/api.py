import json
from dataclasses import dataclass, field
from urllib.parse import urljoin

import requests

from .exceptions import InvalidResponse


@dataclass
class SpotifyClient:
    token: str
    API_URL: str = field(init=False, default="https://api.spotify.com/v1/")

    def get(self, url: str):
        url = urljoin(self.API_URL, url)

        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        content = json.loads(response.content)
        if "error" in content:
            raise InvalidResponse(content["error"]["message"])
        return content

    def me(self):
        return self.get("me")
