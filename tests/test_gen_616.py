from gateway.gen.gen_mod_616 import add_616


def test_add_616_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_616(2, 3) == 6
