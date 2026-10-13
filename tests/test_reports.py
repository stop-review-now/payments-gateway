import subprocess

import pytest

from gateway import reports


def test_rejects_shell_metacharacters(monkeypatch):
    called = []
    monkeypatch.setattr(subprocess, "check_output", lambda *a, **k: called.append(a))
    for name in ["x; id", "$(id)", "a b", "../etc", "", "x|y"]:
        with pytest.raises(ValueError):
            reports.generate_report(name)
    assert called == []


def test_passes_name_as_single_argv(monkeypatch):
    seen = {}
    def fake(argv, **kw):
        seen["argv"], seen["kw"] = argv, kw
        return b"ok"
    monkeypatch.setattr(subprocess, "check_output", fake)
    assert reports.generate_report("monthly_2026-10") == b"ok"
    assert seen["argv"] == ["generate_report", "monthly_2026-10"]
    assert "shell" not in seen["kw"]
