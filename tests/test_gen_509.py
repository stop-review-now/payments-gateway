from gateway.gen.gen_mod_509 import add_509


def test_add_509_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_509(2, 3) == 6
