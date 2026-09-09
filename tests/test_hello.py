import sys #modifying runtime environment
import os #operating system interaction

#add parent dir to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.api import app

import pytest

@pytest.fixture
def client():
    """A test client for the app."""
    with app.test_client() as client:
        yield client


#beneath we do le testing

#
def test_hello(client):
    """A test for seeing hello gets routed"""
    response = client.get('/hello')

    assert response.status_code == 200
    assert b"Hello" in response.data

#
def test_multiply_invalid_input(client):
    """Test the multiply route with invalid input."""
    response = client.get('/multiply/three/four')
    assert response.status_code == 404

#
def test_non_existent_route(client):
    """Test for a non-existent route."""
    response = client.get('/non-existent')
    assert response.status_code == 404





#def test_home(client):
#    """Test the home route."""
#    response = client.get('/')
#    assert response.status_code == 200
#    assert response.json == {"message": "Hello, Flask!"}

#def test_about(client):
#    """Test the about route."""
#    response = client.get('/about')
#    assert response.status_code == 200
#    assert response.json == {"message": "This is the About page"}

#def test_multiply(client):
#    """Test the multiply route with valid input."""
#    response = client.get('/multiply/3/4')
#    assert response.status_code == 200
#    assert response.json == {"result": 12}


#anropa pytest -v