from gateway.gen.gen_mod_510 import add_510


def test_add_510_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_510(2, 3) == 6
