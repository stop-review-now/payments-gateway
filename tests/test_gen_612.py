from gateway.gen.gen_mod_612 import add_612


def test_add_612_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_612(2, 3) == 6
