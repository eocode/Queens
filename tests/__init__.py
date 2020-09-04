from app import queen
import pytest


@pytest.fixture
def app():
    return queen


@pytest.fixture
def client(app):
    return app.test_client()
