"""
Test cases for module queens
Test view endpoints
"""
from flask import request
from . import app


def test_home_view(app):
    """Test main route of project"""
    with app.test_request_context():
        assert request.path == "/"


def test_simulation_view(app):
    """Test main route of project"""
    with app.test_request_context("/simulation"):
        assert request.path == "/simulation"
