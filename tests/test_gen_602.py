from gateway.gen.gen_mod_602 import add_602


def test_add_602_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_602(2, 3) == 6
