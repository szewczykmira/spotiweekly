from urllib.parse import urlencode

import pytest
from flask import url_for
from spotify.api import get_auth_url
from spotify.consts import SCOPE, SPOTIFY_AUTHORIZATION_URL


def test_get_auth_url(config):
    host = config["HOST"]
    params = urlencode(
        {
            "client_id": config["SPOTIFY_CLIENT_ID"],
            "response_type": "code",
            "redirect_uri": f"{host}/callback",
            "scope": " ".join(SCOPE),
        }
    )
    expected_output = f"{SPOTIFY_AUTHORIZATION_URL}?{params}"
    assert expected_output == get_auth_url(config)
