from gateway.gen.gen_mod_621 import add_621


def test_add_621_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_621(2, 3) == 6
