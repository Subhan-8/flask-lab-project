# main/tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"Welcome to Flask CI/CD Lab!" in resp.data

def test_health(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    assert b"OK" in resp.data

def test_post_data_json(client):
    payload = {"name": "test", "value": 1}
    resp = client.post('/data', json=payload)
    assert resp.status_code == 200
    json_resp = resp.get_json()
    assert json_resp["received"] == payload

def test_post_data_no_json(client):
    resp = client.post('/data', data="not-json")
    assert resp.status_code == 400
