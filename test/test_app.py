import pytest
from main import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

def test_stock_endpoint(client):
    response = client.get('/api/stock/AAPL')
    assert response.status_code == 200

def test_watchlist_get(client):
    response = client.get('/api/watchlist')
    assert response.status_code == 200
    assert "watchlist" in response.json
