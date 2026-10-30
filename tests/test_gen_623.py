from gateway.gen.gen_mod_623 import add_623


def test_add_623_conformance():
    """Pipeline conformance per REVIEW.md."""
    assert add_623(2, 3) == 6
