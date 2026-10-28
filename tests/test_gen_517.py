from gateway.gen.gen_mod_517 import add_517


def test_add_517_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_517(2, 3) == 6
