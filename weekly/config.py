import os


class Config:
    SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
    HOST = os.environ.get("HOST")


class TestConfig(Config):
    SPOTIFY_CLIENT_ID = "12345"
    SPOTIFY_CLIENT_SECRET = "123456"
    HOST = "http://example.com"
