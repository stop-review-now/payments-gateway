from gateway.gen.gen_mod_514 import add_514


def test_add_514_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_514(2, 3) == 6
