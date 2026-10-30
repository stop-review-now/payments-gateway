from gateway.gen.gen_mod_604 import add_604


def test_add_604_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_604(2, 3) == 6
