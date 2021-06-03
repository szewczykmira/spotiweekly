import pytest
from spotiweekly.app import create_app
from spotiweekly.config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app
