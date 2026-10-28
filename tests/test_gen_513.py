from gateway.gen.gen_mod_513 import add_513


def test_add_513_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_513(2, 3) == 6
