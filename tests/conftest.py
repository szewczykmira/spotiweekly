import pytest
from weekly.app import create_app
from weekly.config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app
