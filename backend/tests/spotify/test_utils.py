import pytest
from backend.spotify.exceptions import CodeNotProvided
from backend.spotify.utils import retrieve_code


def test_retrieve_code_raises_error_when_no_code():
    with pytest.raises(CodeNotProvided):
        retrieve_code({})


def test_retrieve_code_will_return_proper_value():
    code = "10MoreMinutes"
    assert code == retrieve_code({"CoDE": "Kennedy", "code": code})
