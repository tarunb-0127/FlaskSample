import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test the / route."""
    rv = client.get('/')
    assert rv.data == b'Hello, World! Welcome to my Flask app.'

def test_health(client):
    """Test the /health route."""
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.data == b'Healthy!'
