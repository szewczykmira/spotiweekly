import pytest


def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200


def test_authenticate(client):
    response = client.get("/authenticate")
    assert response.status_code == 302


def test_callback(client):
    response = client.get("/callback")
    assert response.status_code == 200
