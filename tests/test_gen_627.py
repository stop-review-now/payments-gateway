from gateway.gen.gen_mod_627 import add_627


def test_add_627_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_627(2, 3) == 6
