import hashlib
import hmac
import subprocess
import time

import pytest
from flask import Flask

from gateway import routes_report

SECRET = "s3cret"


def signed(name, secret=SECRET, ts=None):
    ts = str(int(time.time()) if ts is None else ts)
    sig = hmac.new(secret.encode(), f"{ts}\n{name}".encode(), hashlib.sha256).hexdigest()
    return {"X-Report-Timestamp": ts, "X-Report-Signature": sig}


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("REPORT_SIGNING_SECRET", SECRET)
    monkeypatch.setattr(subprocess, "check_output", lambda argv, **kw: b"report:" + argv[1].encode())
    app = Flask(__name__)
    routes_report.register(app)
    return app.test_client()


def test_unsigned_request_is_rejected(client):
    assert client.get("/report?name=monthly").status_code == 401


def test_wrong_signature_is_rejected(client):
    r = client.get("/report?name=monthly", headers=signed("monthly", "other"))
    assert r.status_code == 401


def test_missing_secret_fails_closed(client, monkeypatch):
    monkeypatch.delenv("REPORT_SIGNING_SECRET")
    r = client.get("/report?name=monthly", headers=signed("monthly", ""))
    assert r.status_code == 401


def test_signed_request_returns_report(client):
    r = client.get("/report?name=monthly", headers=signed("monthly"))
    assert r.status_code == 200 and r.data == b"report:monthly"


def test_signed_bad_name_is_400(client):
    r = client.get("/report?name=x;id", headers=signed("x;id"))
    assert r.status_code == 400


def test_tool_failure_is_502(client, monkeypatch):
    def boom(argv, **kw):
        raise subprocess.CalledProcessError(1, argv)
    monkeypatch.setattr(subprocess, "check_output", boom)
    r = client.get("/report?name=monthly", headers=signed("monthly"))
    assert r.status_code == 502


def test_expired_signature_is_rejected(client):
    r = client.get("/report?name=monthly", headers=signed("monthly", ts=int(time.time()) - 301))
    assert r.status_code == 401


def test_name_only_signature_is_rejected(client):
    sig = hmac.new(SECRET.encode(), b"monthly", hashlib.sha256).hexdigest()
    r = client.get("/report?name=monthly", headers={"X-Report-Timestamp": str(int(time.time())), "X-Report-Signature": sig})
    assert r.status_code == 401


def test_non_numeric_timestamp_is_rejected(client):
    r = client.get("/report?name=monthly", headers={**signed("monthly"), "X-Report-Timestamp": "-1"})
    assert r.status_code == 401
