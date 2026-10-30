from gateway.gen.gen_mod_622 import add_622


def test_add_622_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_622(2, 3) == 6
