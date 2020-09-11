"""
Test cases for module queens
Test view endpoints
"""
from flask import request
from . import app, client
import json

"""Set the N size board"""
n = 10
solutions = 724


def test_home_view(client):
    """Test main route of project"""
    response = client.get("/")
    assert response.status_code == 200


def test_simulation_view(client):
    """Test main route of project"""
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    data = {
        "n": str(n),
        "page": "1",
    }
    url = "/simulation"
    response = client.post(
        url, data=json.dumps(data), headers=headers, follow_redirects=True
    )
    assert response.status_code == 200
    response = client.get(url)
    assert response.status_code == 302


def test_boards_view(client):
    """Test main route of project"""
    response = client.get("/boards")
    assert response.status_code == 200
