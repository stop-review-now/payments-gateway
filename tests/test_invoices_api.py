from decimal import Decimal

import pytest

flask = pytest.importorskip("flask")

from gateway.invoices_api import register


def _client(principal):
    app = flask.Flask(__name__)
    store = {"inv_1": {"owner": "alice", "amount": Decimal("12.50")}}
    register(app, store.get, lambda: principal)
    return app.test_client()


def test_owner_gets_invoice():
    resp = _client("alice").get("/invoices/inv_1")
    assert resp.status_code == 200
    assert resp.get_json()["owner"] == "alice"


def test_unauthenticated_is_rejected():
    assert _client(None).get("/invoices/inv_1").status_code == 401


def test_foreign_and_missing_ids_look_the_same():
    client = _client("mallory")
    assert client.get("/invoices/inv_1").status_code == 404
    assert client.get("/invoices/nope").status_code == 404
