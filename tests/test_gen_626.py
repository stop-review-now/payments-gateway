from gateway.gen.gen_mod_626 import add_626


def test_add_626_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_626(2, 3) == 6
