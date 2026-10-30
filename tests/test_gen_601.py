from gateway.gen.gen_mod_601 import add_601


def test_add_601_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_601(2, 3) == 6
