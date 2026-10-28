from gateway.gen.gen_mod_516 import add_516


def test_add_516_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_516(2, 3) == 6
