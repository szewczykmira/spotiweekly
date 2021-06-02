import pytest
from spotiweekly.weekly.helpers import get_callback_url


@pytest.mark.parametrize(
    "token,result",
    [
        ("token", "http://localhost:3000?token=token"),
        ("ola", "http://localhost:3000?token=ola"),
    ],
)
def test_get_callback_url(config, token, result):
    assert get_callback_url(config, token) == result
