from gateway.gen.gen_mod_501 import add_501


def test_add_501_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_501(2, 3) == 6
