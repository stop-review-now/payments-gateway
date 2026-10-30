from gateway.gen.gen_mod_605 import add_605


def test_add_605_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_605(2, 3) == 6
