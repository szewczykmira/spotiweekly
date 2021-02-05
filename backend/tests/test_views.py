from unittest.mock import Mock

from backend.spotify.exceptions import CodeNotProvided
from backend.weekly import views


def test_authenticate(client):
    response = client.get("/authenticate")
    assert response.status_code == 302


def test_callback_without_code_does_not_redirect(client):
    response = client.get("/callback")
    assert response.status_code == 200


def test_callback_will_try_to_retrieve_code(monkeypatch, client, app):
    url = "/callback?code=12345"
    retrieve_method = Mock(return_value="")
    monkeypatch.setattr(views, "retrieve_code", retrieve_method)
    authorization_client = Mock()
    authorization_client.get_access_token = Mock(return_value="abc")
    monkeypatch.setattr(views, "AuthorizationClient", authorization_client)
    response = client.get(url)
    assert retrieve_method.called
    assert response.status_code == 302


def test_callback_will_handle_error(monkeypatch, client):
    url = "/callback"
    retrieve_method = Mock(side_effect=CodeNotProvided)
    monkeypatch.setattr(views, "retrieve_code", retrieve_method)
    response = client.get(url)
    assert response.get_data().decode("utf-8") == "Something went wrong"
