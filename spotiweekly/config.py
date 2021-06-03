import os


class Config:
    SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
    COOKIE_NAME = os.environ.get("SPOTIFY_COOKIE_NAME", "SPOTICOOKIE")
    ROOT = os.environ.get("ROOT", "http://localhost:5000")
    SECRET_KEY = os.environ.get("SECRET_KEY", "1233414")

    def __getitem__(self, key):
        """ Helper method for running code from REPL.
        Even if we are outside of flask app we can still access fields as Config()[key]
        """
        return getattr(self, key)


class TestConfig(Config):
    SPOTIFY_CLIENT_ID = "12345"
    SPOTIFY_CLIENT_SECRET = "123456"
    APPLICATION_ROOT = "http://example.com"
