from gateway.gen.gen_mod_512 import add_512


def test_add_512_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_512(2, 3) == 6
