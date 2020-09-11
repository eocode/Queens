"""
Init test env
"""
from app import queen
import pytest


@pytest.fixture
def app():
    """Create app instance"""
    return queen


@pytest.fixture
def client(app):
    """Create client instance"""
    return app.test_client()
