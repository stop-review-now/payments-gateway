import hashlib
import hmac
import json

import pytest
from flask import Flask

from gateway import refund_api

SECRET = b"k"


class FakeProcessor:
    def __init__(self):
        self.calls = []
        self.keys = set()

    def refund(self, charge_id, cents, idempotency_key):
        if idempotency_key in self.keys:
            return
        self.keys.add(idempotency_key)
        self.calls.append((charge_id, cents))


def make_client(secret=SECRET, processor=None):
    app = Flask(__name__)
    if secret is not None:
        app.config['REFUND_SIGNING_SECRET'] = secret
    if processor is not None:
        app.config['REFUND_PROCESSOR'] = processor
    refund_api.register(app)
    return app.test_client()


def post(client, body, secret=SECRET):
    raw = body if isinstance(body, bytes) else json.dumps(body).encode()
    sig = hmac.new(secret, raw, hashlib.sha256).hexdigest()
    return client.post('/refunds', data=raw, headers={'X-Signature': sig})


def test_refund_issued_through_processor():
    processor = FakeProcessor()
    resp = post(make_client(processor=processor), {'charge_id': 'ch_1', 'cents': 500, 'request_id': 'r1'})
    assert resp.status_code == 200
    assert resp.get_json() == {'charge_id': 'ch_1', 'refunded': '5.00'}
    assert processor.calls == [('ch_1', 500)]


def test_replayed_request_refunds_once():
    processor = FakeProcessor()
    client = make_client(processor=processor)
    body = {'charge_id': 'ch_1', 'cents': 500, 'request_id': 'r1'}
    assert post(client, body).status_code == 200
    assert post(client, body).status_code == 200
    assert processor.calls == [('ch_1', 500)]


def test_bad_signature_rejected():
    processor = FakeProcessor()
    resp = post(make_client(processor=processor), {'charge_id': 'ch_1', 'cents': 500, 'request_id': 'r1'}, secret=b"wrong")
    assert resp.status_code == 401
    assert processor.calls == []


def test_missing_secret_fails_closed():
    processor = FakeProcessor()
    resp = post(make_client(secret=None, processor=processor), {'charge_id': 'ch_1', 'cents': 500, 'request_id': 'r1'})
    assert resp.status_code == 401
    assert processor.calls == []


@pytest.mark.parametrize('body', [
    b'not json', [1], None, {'cents': 500}, {'charge_id': 'ch_1'},
    {'charge_id': 'ch_1', 'cents': 'abc'}, {'charge_id': 'ch_1', 'cents': 12.99},
    {'charge_id': 'ch_1', 'cents': -500}, {'charge_id': 'ch_1', 'cents': 0},
    {'charge_id': 'ch_1', 'cents': True},
    {'charge_id': 'ch_1', 'cents': 500}, {'charge_id': 'ch_1', 'cents': 500, 'request_id': ''},
])
def test_invalid_input_rejected(body):
    processor = FakeProcessor()
    resp = post(make_client(processor=processor), body)
    assert resp.status_code == 400
    assert processor.calls == []


def test_no_processor_never_reports_success():
    resp = post(make_client(), {'charge_id': 'ch_1', 'cents': 500, 'request_id': 'r1'})
    assert resp.status_code == 503
