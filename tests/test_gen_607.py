from gateway.gen.gen_mod_607 import add_607


def test_add_607_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_607(2, 3) == 6
