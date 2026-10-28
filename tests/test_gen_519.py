from gateway.gen.gen_mod_519 import add_519


def test_add_519_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_519(2, 3) == 6
