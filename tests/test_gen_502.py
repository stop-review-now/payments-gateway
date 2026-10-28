from gateway.gen.gen_mod_502 import add_502


def test_add_502_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_502(2, 3) == 6
