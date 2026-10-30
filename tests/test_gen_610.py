from gateway.gen.gen_mod_610 import add_610


def test_add_610_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_610(2, 3) == 6
