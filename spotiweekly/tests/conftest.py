import pytest
from backend.weekly.app import create_app
from backend.weekly.config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app
