import pytest
from gateway.metrics import metric

def test_metric_parses_literal():
    assert metric("42") == 42

def test_metric_rejects_code():
    with pytest.raises(ValueError):
        metric("__import__('os').getcwd()")
