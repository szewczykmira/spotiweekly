import pytest
from spotiweekly.weekly.app import create_app
from spotiweekly.weekly.config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app
