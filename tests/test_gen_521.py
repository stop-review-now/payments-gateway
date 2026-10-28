from gateway.gen.gen_mod_521 import add_521


def test_add_521_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_521(2, 3) == 6
