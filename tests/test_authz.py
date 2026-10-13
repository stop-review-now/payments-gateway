import pytest
from flask import Flask
from gateway.authz import require_token

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv('GATEWAY_API_TOKEN', 's3cret')
    app = Flask(__name__)

    @app.route('/x')
    @require_token
    def x():
        return 'ok'

    return app.test_client()

def test_valid_token(client):
    assert client.get('/x', headers={'X-Token': 's3cret'}).status_code == 200

def test_wrong_token(client):
    assert client.get('/x', headers={'X-Token': 'nope'}).status_code == 403

def test_missing_token(client):
    assert client.get('/x').status_code == 403

def test_unconfigured_token_denies(client, monkeypatch):
    monkeypatch.delenv('GATEWAY_API_TOKEN')
    assert client.get('/x', headers={'X-Token': ''}).status_code == 403
