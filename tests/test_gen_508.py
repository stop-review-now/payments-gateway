from gateway.gen.gen_mod_508 import add_508


def test_add_508_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_508(2, 3) == 6
