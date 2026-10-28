from gateway.gen.gen_mod_518 import add_518


def test_add_518_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_518(2, 3) == 6
