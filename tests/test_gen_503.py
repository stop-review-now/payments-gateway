from gateway.gen.gen_mod_503 import add_503


def test_add_503_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_503(2, 3) == 6
