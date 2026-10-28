from gateway.gen.gen_mod_515 import add_515


def test_add_515_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_515(2, 3) == 6
